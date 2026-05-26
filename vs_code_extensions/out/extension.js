"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.activate = activate;
// @ts-ignore
const vscode = require("vscode");
function activate(context) {
    const diagnostics = vscode.languages.createDiagnosticCollection('ai');
    // 1. Text change listener for static diagnostics
    vscode.workspace.onDidChangeTextDocument(async (event) => {
        if (event.document.uri.scheme !== 'file')
            return;
        const text = event.document.getText();
        try {
            const response = await fetch('http://localhost:5050', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    code: text,
                    path: event.document.fileName
                })
            });
            const result = (await response.json());
            const issues = result.static?.issues || [];
            const vscodeDiagnostics = [];
            for (const issue of issues) {
                const diagnostic = new vscode.Diagnostic(new vscode.Range(0, 0, 0, 1), issue, vscode.DiagnosticSeverity.Warning);
                vscodeDiagnostics.push(diagnostic);
            }
            diagnostics.set(event.document.uri, vscodeDiagnostics);
        }
        catch (error) {
            console.error("Backend fetch error:", error);
        }
    });
    // 2. Command definition for optimizing code
    const optimizeCommand = vscode.commands.registerCommand('ai.optimize', async () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor)
            return;
        const text = editor.document.getText();
        try {
            const response = await fetch('http://localhost:5050', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    code: text,
                    path: editor.document.fileName
                })
            });
            const result = (await response.json());
            const optimized = result.optimized;
            if (optimized) {
                await editor.edit((editBuilder) => {
                    const fullRange = new vscode.Range(editor.document.positionAt(0), editor.document.positionAt(text.length));
                    editBuilder.replace(fullRange, optimized);
                });
                vscode.window.showInformationMessage('Code Optimized');
            }
            else {
                vscode.window.showWarningMessage('No optimization returned from backend.');
            }
        }
        catch (error) {
            vscode.window.showErrorMessage('Failed to connect to optimization backend.');
            console.error(error);
        }
    });
    context.subscriptions.push(optimizeCommand);
}

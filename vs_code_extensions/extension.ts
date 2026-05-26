import * as vscode from 'vscode';
import axios from 'axios';

export function activate(context: vscode.ExtensionContext) {
    let disposable = vscode.commands.registerCommand('ai.optimize', async () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showErrorMessage('Open the file first!');
            return;
        }

        const selection = editor.selection;
        const text = editor.document.getText(selection) || editor.document.getText();

        if (!text || text.trim() === "") {
            vscode.window.showWarningMessage('Select some code to optimize!');
            return;
        }

        vscode.window.showInformationMessage('Optimizing via Ubuntu Backend...');

        try {
            const response = await axios.post('[http://127.0.0.1:5050/](http://127.0.0.1:5050/)', { 
                code: text,
                path: editor.document.fileName 
            });
            
            const optimizedCode = response.data.optimized;

            if (optimizedCode) {
                await editor.edit(editBuilder => {
                    if (!selection.isEmpty) {
                        editBuilder.replace(selection, optimizedCode);
                    } else {
                        const fullRange = new vscode.Range(
                            editor.document.positionAt(0),
                            editor.document.positionAt(editor.document.getText().length)
                        );
                        editBuilder.replace(fullRange, optimizedCode);
                    }
                });
                vscode.window.showInformationMessage('Code Optimized Successfully! ');
            } else {
                vscode.window.showErrorMessage('Backend data format mismatch!');
            }
        } catch (error) {
            vscode.window.showErrorMessage('Connection failed! Please ensure the backend is running.');
        }
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}
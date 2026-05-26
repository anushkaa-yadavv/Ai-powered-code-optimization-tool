const vscode = require('vscode');
const axios = require('axios');

function activate(context) {
    let disposable = vscode.commands.registerCommand('ai.optimize', async () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor) return;

        const text = editor.document.getText();
        
        // UI mein loading dikhane ke liye
        await vscode.window.withProgress({
            location: vscode.ProgressLocation.Notification,
            title: "AI Code Engine is optimizing...",
            cancellable: false
        }, async (progress) => {
            try {
                // Yahan tumhara FastAPI server (server.py) call hoga
                const response = await axios.post('http://127.0.0.1:5050/analyze', {
                    code: text,
                    path: editor.document.fileName
                });

                const optimizedCode = response.data.optimized;

                if (optimizedCode) {
                    const fullRange = new vscode.Range(
                        editor.document.positionAt(0),
                        editor.document.positionAt(text.length)
                    );
                    await editor.edit(editBuilder => {
                        editBuilder.replace(fullRange, optimizedCode);
                    });
                    vscode.window.showInformationMessage('Code optimized successfully!');
                }
            } catch (error) {
                vscode.window.showErrorMessage('Backend Error: Check if FastAPI is running on port 5050');
            }
        });
    });

    context.subscriptions.push(disposable);
}

exports.activate = activate;

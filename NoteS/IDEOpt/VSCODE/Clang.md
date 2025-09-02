- tasks.json
```
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Build",
            "type": "shell",
            "command": "clang",
            "args": [
                "-o",
                "main.exe",
                "main.cpp"
            ],
            "group": "build",
            "options": {
                "cwd": "${workspaceFolder}"
            },
            "problemMatcher": "$gcc"
        }
    ]
}
```
***
- launch.json
```
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "(Windows) Launch",
      "type": "lldb",
      "request": "launch",
      "program": "${workspaceFolder}/main.exe",
      "args": [],
      "cwd":"${workspaceFolder}",
      "console": "integratedTerminal"
    }
  ]
}
```
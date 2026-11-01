[Setup]
AppName=Markdown Converter
AppVersion=2.3.0
AppPublisher=vantunes
DefaultDirName={autopf}\Markdown Converter
DefaultGroupName=Markdown Converter
OutputDir=output
OutputBaseFilename=MarkdownConverterSetup_v2.3.0
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Files]
Source: "..\dist\main\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Markdown Converter"; Filename: "{app}\main.exe"

Name: "{autodesktop}\Markdown Converter"; Filename: "{app}\main.exe"

[Run]
Filename: "{app}\main.exe"; Description: "Executar Markdown Converter"; Flags: nowait postinstall skipifsilent
# Function
function listHiddenFiles { Get-ChildItem -Force }

# Set Alias
Set-Alias -Name ls -Value Get-ChildItem
Set-Alias -Name ll -Value Get-ChildItem
Set-Alias -Name la -Value listHiddenFiles


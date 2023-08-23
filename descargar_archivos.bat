@echo off

for /f "usebackq tokens=1-4 delims=," %%a in ("indices_refraccion.csv") do (
    set "category=%%a"
    set "material_name=%%b"
    set "yaml_url=%%d"
    
    if not exist "!category!" (
        mkdir "!category!"
    )

    curl -o "!category!\!material_name!.yml" "!yaml_url!"
)


import os
import argparse
import sys
import xml.etree.ElementTree as ET


def get_default_config(run_manager):
    config = run_manager.find("configuration")
    if config is None:
        return {}
    defaults = {
        "module_name": config.find("module").attrib.get("name", "")
        if config.find("module") is not None
        else "",
        "envs": [env.attrib for env in config.find("envs") or []],
        "SDK_HOME": config.find("option[@name='SDK_HOME']").attrib.get("value", "")
        if config.find("option[@name='SDK_HOME']") is not None
        else "",
        "IS_MODULE_SDK": config.find("option[@name='IS_MODULE_SDK']").attrib.get("value", "true")
        if config.find("option[@name='IS_MODULE_SDK']") is not None
        else "true",
        "ADD_CONTENT_ROOTS": config.find("option[@name='ADD_CONTENT_ROOTS']").attrib.get(
            "value", "true"
        )
        if config.find("option[@name='ADD_CONTENT_ROOTS']") is not None
        else "true",
        "ADD_SOURCE_ROOTS": config.find("option[@name='ADD_SOURCE_ROOTS']").attrib.get(
            "value", "true"
        )
        if config.find("option[@name='ADD_SOURCE_ROOTS']") is not None
        else "true",
        "INTERPRETER_OPTIONS": config.find("option[@name='INTERPRETER_OPTIONS']").attrib.get(
            "value", ""
        )
        if config.find("option[@name='INTERPRETER_OPTIONS']") is not None
        else "",
        "PARENT_ENVS": config.find("option[@name='PARENT_ENVS']").attrib.get("value", "true")
        if config.find("option[@name='PARENT_ENVS']") is not None
        else "true",
        "WORKING_DIRECTORY": config.find("option[@name='WORKING_DIRECTORY']").attrib.get(
            "value", "$PROJECT_DIR$"
        )
        if config.find("option[@name='WORKING_DIRECTORY']") is not None
        else "$PROJECT_DIR$",
        "SHOW_COMMAND_LINE": config.find("option[@name='SHOW_COMMAND_LINE']").attrib.get(
            "value", "false"
        )
        if config.find("option[@name='SHOW_COMMAND_LINE']") is not None
        else "false",
        "EMULATE_TERMINAL": config.find("option[@name='EMULATE_TERMINAL']").attrib.get(
            "value", "false"
        )
        if config.find("option[@name='EMULATE_TERMINAL']") is not None
        else "false",
        "MODULE_MODE": config.find("option[@name='MODULE_MODE']").attrib.get("value", "false")
        if config.find("option[@name='MODULE_MODE']") is not None
        else "false",
        "REDIRECT_INPUT": config.find("option[@name='REDIRECT_INPUT']").attrib.get("value", "false")
        if config.find("option[@name='REDIRECT_INPUT']") is not None
        else "false",
        "INPUT_FILE": config.find("option[@name='INPUT_FILE']").attrib.get("value", "")
        if config.find("option[@name='INPUT_FILE']") is not None
        else "",
        "ENV_FILES": config.find("option[@name='ENV_FILES']").attrib.get("value", "")
        if config.find("option[@name='ENV_FILES']") is not None
        else "",
    }
    return defaults


def add_run_config_to_workspace(
    workspace_path,
    script_path,
    config_name="DefaultRun",
    params="",
    interpreter_path=None,
):
    tree = ET.parse(workspace_path)
    root = tree.getroot()
    run_manager = root.find(".//component[@name='RunManager']")
    if run_manager is None:
        print("Nie znaleziono sekcji RunManager w workspace.xml")
        return

    defaults = get_default_config(run_manager)
    sdk_home = interpreter_path or defaults["SDK_HOME"] or sys.executable
    script_abs_path = os.path.abspath(script_path)

    config = ET.Element(
        "configuration",
        {
            "name": config_name,
            "type": "PythonConfigurationType",
            "factoryName": "Python",
            "nameIsGenerated": "true",
        },
    )
    ET.SubElement(config, "module", {"name": defaults["module_name"]})
    ET.SubElement(config, "option", {"name": "ENV_FILES", "value": defaults["ENV_FILES"]})
    ET.SubElement(
        config,
        "option",
        {"name": "INTERPRETER_OPTIONS", "value": defaults["INTERPRETER_OPTIONS"]},
    )
    ET.SubElement(config, "option", {"name": "PARENT_ENVS", "value": defaults["PARENT_ENVS"]})
    envs = ET.SubElement(config, "envs")
    for env in defaults["envs"]:
        ET.SubElement(envs, "env", env)
    ET.SubElement(config, "option", {"name": "SDK_HOME", "value": sdk_home})
    ET.SubElement(
        config,
        "option",
        {"name": "WORKING_DIRECTORY", "value": defaults["WORKING_DIRECTORY"]},
    )
    ET.SubElement(config, "option", {"name": "IS_MODULE_SDK", "value": defaults["IS_MODULE_SDK"]})
    ET.SubElement(
        config,
        "option",
        {"name": "ADD_CONTENT_ROOTS", "value": defaults["ADD_CONTENT_ROOTS"]},
    )
    ET.SubElement(
        config,
        "option",
        {"name": "ADD_SOURCE_ROOTS", "value": defaults["ADD_SOURCE_ROOTS"]},
    )
    ET.SubElement(config, "option", {"name": "SCRIPT_NAME", "value": script_abs_path})
    ET.SubElement(config, "option", {"name": "PARAMETERS", "value": params})
    ET.SubElement(
        config,
        "option",
        {"name": "SHOW_COMMAND_LINE", "value": defaults["SHOW_COMMAND_LINE"]},
    )
    ET.SubElement(
        config,
        "option",
        {"name": "EMULATE_TERMINAL", "value": defaults["EMULATE_TERMINAL"]},
    )
    ET.SubElement(config, "option", {"name": "MODULE_MODE", "value": defaults["MODULE_MODE"]})
    ET.SubElement(
        config,
        "option",
        {"name": "REDIRECT_INPUT", "value": defaults["REDIRECT_INPUT"]},
    )
    ET.SubElement(config, "option", {"name": "INPUT_FILE", "value": defaults["INPUT_FILE"]})
    ET.SubElement(config, "method", {"v": "2"})

    run_manager.append(config)
    tree.write(workspace_path, encoding="utf-8", xml_declaration=True)
    print(f"Konfiguracja dodana do: {workspace_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Dodaje konfigurację uruchomienia PyCharm do workspace.xml na podstawie domyślnego SDK."
    )
    parser.add_argument("script_path", help="Ścieżka do pliku Python")
    parser.add_argument("--config_name", default="DefaultRun", help="Nazwa konfiguracji")
    parser.add_argument("--params", default="", help="Parametry uruchomienia")
    parser.add_argument("--interpreter", default=None, help="Ścieżka do interpretera Pythona")
    parser.add_argument(
        "--workspace",
        default=os.path.join(".idea", "workspace.xml"),
        help="Ścieżka do workspace.xml",
    )
    args = parser.parse_args()
    add_run_config_to_workspace(
        args.workspace,
        args.script_path,
        config_name=args.config_name,
        params=args.params,
        interpreter_path=args.interpreter,
    )

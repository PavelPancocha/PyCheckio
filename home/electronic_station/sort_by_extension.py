def sort_by_ext(files: list[str]) -> list[str]:
    name_extension_split: list[tuple[str, str]] = []
    without_extension: list[str] = []
    without_name: list[str] = []

    for file in files:
        try:
            file_name, extension = file.rsplit(".", maxsplit=1)

        except ValueError:
            without_extension.append(file)
        else:
            if file_name == "":
                without_name.append(file)
            else:
                name_extension_split.append((file_name, extension))

    name_extension_split.sort(key=lambda x: (x[1], x[0]))
    without_extension.sort()
    without_name.sort()
    return without_name + without_extension + [f"{name}.{extension}" for name, extension in name_extension_split]

Window(
        Const('Enter your name, please'),
        TextInput(
            id='fill_name',
            on_success=name_correct_nandler,
            on_error=name_error_nandler
            ),
        state=AccountSG.fill_name
    )

Window(
        Const('Change your name, please'),
        TextInput(
            id='change_name',
            on_success=name_correct_nandler,
            on_error=name_error_nandler
            ),
        state=AccountSG.change_name
    )

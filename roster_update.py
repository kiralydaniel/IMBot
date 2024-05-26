import utility

bot = utility.bot

spreadsheet = utility.spreadsheet

# Get Sheet1
runs = utility.sheet1

# Get Sheet2
balance = utility.sheet2

# Update names in Sheet from txt
@bot.command()
@utility.is_admin()
async def update(ctx, day: str):
    day = day.lower()
    
    if day == "friday":
        file_path = utility.friday_txt_path
        column = 'A'
    elif day == "saturday":
        file_path = utility.saturday_txt_path
        column = 'D'
    else:
        await ctx.send("Invalid option. Please choose 'friday' or 'saturday'.")
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        names = file.readlines()
        names = [name.strip() for name in names]  # Remove newline characters

    # Write names to the appropriate column starting from the second row
    runs.update(f'{column}2:{column}{len(names) + 1}', [[name] for name in names])

    await utility.send_embed_private(ctx, f"**{day.capitalize()}** boost updated in the sheet!")



# Discord command to boost a user's gold in Balance based on Sheet1 data
@bot.command()
@utility.is_admin()
async def balance1(ctx):
    # Get names and numbers from Sheet1 from row 2 to row 17
    names_sheet1 = runs.col_values(1)[1:17]
    numbers_sheet1 = runs.col_values(3)[1:17]

    # Iterate over names and corresponding numbers
    for name, number in zip(names_sheet1, numbers_sheet1):
        # Find the row in Sheet2 corresponding to the user's name
        try:
            row_index_sheet2 = balance.col_values(4).index(name) + 1
        except ValueError:
            await utility.send_embed_private(ctx, f"Name '{name}' not found in Balance.")
            continue

        # Get the existing number from Sheet2
        existing_number = balance.cell(row_index_sheet2, 2).value
        if existing_number is None or existing_number == '':
            existing_number = 0  # Set default value to 0 if cell is empty

        # Clean up the number (remove whitespace and commas)
        cleaned_number = number.replace(' ', '').replace(',', '')

        # Check if the cleaned number is a valid integer
        try:
            boost_value = int(cleaned_number)
        except ValueError:
            await utility.send_embed_private(ctx, f"Invalid gold value '{number}' for user '{name}'. Skipping...")
            continue

        # Update the number in Sheet2 by adding the cleaned number from Sheet1
        new_number = int(existing_number) + boost_value
        balance.update_cell(row_index_sheet2, 2, new_number)

    await utility.send_embed_private(ctx, "Numbers for **Friday** boost updated in Balance!")


# Discord command to boost a user's gold in Balance based on Sheet1 data
@bot.command()
@utility.is_admin()
async def balance2(ctx):
    # Get names and numbers from Sheet1 from row 2 to row 17
    names_sheet1 = runs.col_values(4)[1:17]
    numbers_sheet1 = runs.col_values(6)[1:17]

    # Iterate over names and corresponding numbers
    for name, number in zip(names_sheet1, numbers_sheet1):
        # Find the row in Sheet2 corresponding to the user's name
        try:
            row_index_sheet2 = balance.col_values(4).index(name) + 1
        except ValueError:
            await utility.send_embed_private(ctx, f"Name **'{name}'** not found in Balance.")
            continue

        # Get the existing number from Sheet2
        existing_number = balance.cell(row_index_sheet2, 2).value
        if existing_number is None or existing_number == '':
            existing_number = 0  # Set default value to 0 if cell is empty

        # Clean up the number (remove whitespace and commas)
        cleaned_number = number.replace(' ', '').replace(',', '')

        # Check if the cleaned number is a valid integer
        try:
            boost_value = int(cleaned_number)
        except ValueError:
            await utility.send_embed_private(ctx, f"Invalid gold value **'{number}'** for user **'{name}'**. Skipping...")
            continue

        # Update the number in Sheet2 by adding the cleaned number from Sheet1
        new_number = int(existing_number) + boost_value
        balance.update_cell(row_index_sheet2, 2, new_number)

    await utility.send_embed_private(ctx, "Numbers for Saturday boost updated in Balance!")



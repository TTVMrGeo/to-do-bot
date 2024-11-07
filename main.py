import config
import discord

# Define the necessary intents
intents = config.INTENTS
client = config.CLIENT

if __name__ == '__main__':
    if config.BOT_TOKEN == "":
        print("Error: No bot token!")
        exit()

# Start
@client.event
async def on_ready():
    print("Bot is online!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Prefix: {}".format(config.BOT_PREFIX)))

@client.command(name='add', aliases=['a'])
async def add(ctx, item):
    try:
        with open('todo.txt', 'a') as f:
            print(item, file=f)
        await ctx.send(f"Added {item} to your todo list!")
        
        with open('todo.txt', 'r') as f:
            todo_list = f.read()  # Read the file content
        if todo_list.strip():  # Check if the file is not empty
            await ctx.send(f"Current todo list:\n{todo_list}")  # Send the content as a message
    except FileNotFoundError:
        await ctx.send("The todo list file was not found!")

@client.command(name='list', aliases=['l'])
async def list(ctx):
    try:
        with open('todo.txt', 'r') as f:
            todo_list = f.readlines()  # Read lines as a list
        if todo_list:  # Check if the list has items
            # Add line numbers to each line
            numbered_list = [f"{i + 1}) {line.strip()}" for i, line in enumerate(todo_list)]
            formatted_list = "\n".join(numbered_list)  # Join lines with newlines
            await ctx.send(formatted_list)  # Send the formatted list
        else:
            await ctx.send("Your todo list is empty!")
    except FileNotFoundError:
        await ctx.send("The todo list file was not found!") 

@client.command(name='remove', aliases=['r'])
async def remove(ctx, item_number: int):
    try:
        with open('todo.txt', 'r') as f:
            todo_list = f.readlines()  # Read all lines into a list

        # Check if the item number is valid
        if 1 <= item_number <= len(todo_list):
            removed_item = todo_list.pop(item_number - 1)  # Remove the specified item

            # Write the updated list back to the file
            with open('todo.txt', 'w') as f:
                f.writelines(todo_list)

            await ctx.send(f"Removed item {item_number}: {removed_item.strip()}")
        else:
            await ctx.send("Invalid item number!")
    except FileNotFoundError:
        await ctx.send("The todo list file was not found!")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@client.command(name='clear', aliases=['c'])
async def clear(ctx):
    try:
        with open('todo.txt', 'w') as f:
            f.write('')  # Clear the file by writing an empty string
        await ctx.send("The todo list has been cleared!")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

client.run(config.BOT_TOKEN)
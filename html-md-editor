import re
import markdown2

# Read the HTML file
with open("template.html", "r") as file:
    html_content = file.read()

# Get the user's input for the message in Markdown format
markdown_message = input("Enter the message in Markdown format: ")

# Convert the Markdown message to HTML
html_message = markdown2.markdown(markdown_message)

# Replace {{ Message }} with the HTML message (case-insensitive)
modified_html = re.sub(r"{{\s*Message\s*}}", html_message, html_content, flags=re.I)

# Write the modified content to a new file named "message.html"
with open("message.html", "w") as file:
    file.write(modified_html)

print("Modified HTML saved to message.html")

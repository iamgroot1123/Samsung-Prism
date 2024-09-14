from pypdf import PdfReader

def add_content(reader, page_number, start_keyword, end_keyword, combined_text, next_line):
    page = reader.pages[page_number]
    text = page.extract_text()

    start_index = text.find(start_keyword)
    end_index = text.find(end_keyword, start_index)

    if start_index != -1 and end_index != -1:
        specific_content = text[start_index:end_index + len(end_keyword)]
        if next_line:
            combined_text += specific_content + "\n"
        else:
            combined_text += specific_content + " "
    else:
        print(f"Specified content not found in Page {page_number}.")

    return combined_text

def add_content_exclude_first_last_continue(reader, page_number, combined_text):
    page = reader.pages[page_number]
    text = page.extract_text()

    lines = text.split("\n")

    if len(lines) > 2:
        lines = lines[1:-1]

    filtered_text = "\n".join(lines)
    combined_text += filtered_text + " "

    return combined_text

def add_content_exclude_first_last_newline(reader, page_number, combined_text):
    page = reader.pages[page_number]
    text = page.extract_text()

    lines = text.split("\n")

    if len(lines) > 2:
        lines = lines[1:-1]

    filtered_text = "\n".join(lines)
    combined_text += filtered_text + "\n"

    return combined_text


reader = PdfReader("rfc3261.pdf")
num_pages = len(reader.pages)

metadata = reader.metadata
for key, value in metadata.items():
    print(f"{key}: {value}")
    
combined_text = ""

combined_text = add_content(reader, 7, "1 Introduction", "protocols by", combined_text, False)
combined_text = add_content_exclude_first_last_continue(reader, 8, combined_text)

for page_num in range(9, 12):
    combined_text = add_content_exclude_first_last_newline(reader, page_num, combined_text)
    
for page_num in range(12, 22):
    combined_text = add_content_exclude_first_last_continue(reader, page_num, combined_text)

combined_text = add_content_exclude_first_last_newline(reader, 22, combined_text)
combined_text = add_content_exclude_first_last_continue(reader, 23, combined_text)

for page_num in range(24, 29):
    combined_text = add_content_exclude_first_last_newline(reader, page_num, combined_text)

for page_num in range(29, 32):
    combined_text = add_content_exclude_first_last_continue(reader, page_num, combined_text)

for page_num in range(32, 36):
    combined_text = add_content_exclude_first_last_newline(reader, page_num, combined_text)

combined_text = add_content_exclude_first_last_continue(reader, 36, combined_text)
combined_text = add_content_exclude_first_last_newline(reader, 37, combined_text)

for page_num in range(38, 41):
    combined_text = add_content_exclude_first_last_continue(reader, page_num, combined_text)

for page_num in range(41, 45):
    combined_text = add_content_exclude_first_last_newline(reader, page_num, combined_text)

combined_text = add_content_exclude_first_last_continue(reader, 45, combined_text)

for page_num in range(46, 49):
    combined_text = add_content_exclude_first_last_newline(reader, page_num, combined_text)

for page_num in range(49, 54):
    combined_text = add_content_exclude_first_last_continue(reader, page_num, combined_text)

combined_text = add_content_exclude_first_last_newline(reader, 54, combined_text)
combined_text = add_content_exclude_first_last_continue(reader, 55, combined_text)

for page_num in range(56, 68):
    combined_text = add_content_exclude_first_last_newline(reader, page_num, combined_text)

for page_num in range(68, 78):
    combined_text = add_content_exclude_first_last_continue(reader, page_num, combined_text)

for page_num in range(78, 82):
    combined_text = add_content_exclude_first_last_newline(reader, page_num, combined_text)

for page_num in range(82, 92):
    combined_text = add_content_exclude_first_last_continue(reader, page_num, combined_text)

for page_num in range(92, 96):
    combined_text = add_content_exclude_first_last_newline(reader, page_num, combined_text)

for page_num in range(96, 98):
    combined_text = add_content_exclude_first_last_continue(reader, page_num, combined_text)

for page_num in range(98, 101):
    combined_text = add_content_exclude_first_last_newline(reader, page_num, combined_text)

combined_text = add_content_exclude_first_last_continue(reader, 101, combined_text)

for page_num in range(102, 104):
    combined_text = add_content_exclude_first_last_newline(reader, page_num, combined_text)

combined_text = add_content_exclude_first_last_continue(reader, 104, combined_text)

for page_num in range(105, 107):
    combined_text = add_content_exclude_first_last_newline(reader, page_num, combined_text)

for page_num in range(107, 114):
    combined_text = add_content_exclude_first_last_continue(reader, page_num, combined_text)

for page_num in range(114, 121):
    combined_text = add_content_exclude_first_last_newline(reader, page_num, combined_text)

for page_num in range(121, 126):
    combined_text = add_content_exclude_first_last_continue(reader, page_num, combined_text)

combined_text = add_content_exclude_first_last_newline(reader, 126, combined_text)

for page_num in range(127, 131):
    combined_text = add_content_exclude_first_last_continue(reader, page_num, combined_text)

combined_text = add_content_exclude_first_last_newline(reader, 131, combined_text)

for page_num in range(132, 134):
    combined_text = add_content_exclude_first_last_continue(reader, page_num, combined_text)

for page_num in range(134, 137):
    combined_text = add_content_exclude_first_last_newline(reader, page_num, combined_text)

combined_text = add_content_exclude_first_last_continue(reader, 137, combined_text)
combined_text = add_content_exclude_first_last_newline(reader, 138, combined_text)

for page_num in range(139, 143):
    combined_text = add_content_exclude_first_last_continue(reader, page_num, combined_text)

for page_num in range(143, 147):
    combined_text = add_content_exclude_first_last_newline(reader, page_num, combined_text)

for page_num in range(147, 150):
    combined_text = add_content_exclude_first_last_continue(reader, page_num, combined_text)

for page_num in range(150, 175):
    combined_text = add_content_exclude_first_last_newline(reader, page_num, combined_text)

for page_num in range(175, 180):
    combined_text = add_content_exclude_first_last_continue(reader, page_num, combined_text)

for page_num in range(180, 201):
    combined_text = add_content_exclude_first_last_newline(reader, page_num, combined_text)

for page_num in range(201, 205):
    combined_text = add_content_exclude_first_last_continue(reader, page_num, combined_text)

for page_num in range(205, 236):
    combined_text = add_content_exclude_first_last_newline(reader, page_num, combined_text)

for page_num in range(236, 254):
    combined_text = add_content_exclude_first_last_continue(reader, page_num, combined_text)

for page_num in range(254, 260):
    combined_text = add_content_exclude_first_last_newline(reader, page_num, combined_text)


with open("rfc3261.txt", "w") as file:
    file.write(combined_text)
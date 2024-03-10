import base64

def url_generator(blob, file_type):
    base64_data = base64.b64encode(blob).decode('utf-8')

    if file_type == 'mp4':
        mime_type = 'video/mp4'
    elif file_type == 'webm':
        mime_type = 'video/webm'
    
    return f'data:{mime_type};base64,{base64_data}'

import qrcode

def generate_qr_code(data, filename="qrcode.png"):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR Code instance
    img = qr.make_image(fill="black", back_color="white")
    
    # Save the image
    img.save(filename)
    print(f"QR code saved as {filename}")

# Example usage
if __name__ == "__main__":
    text_or_url = input("Enter text or URL: ")
    generate_qr_code(text_or_url)
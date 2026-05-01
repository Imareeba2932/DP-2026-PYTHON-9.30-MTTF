import flexui

# 1. Page Title set karein
flexui.title("Mera Naya External App")

# 2. Kuch buttons aur headings add karein
flexui.Text("Yeh test script hai!", size="h1", align="center")
flexui.Button("External Button", variant="primary")

# 3. Server start karein
if __name__ == "__main__":
    flexui.render()
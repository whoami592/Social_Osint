import tkinter as tk
from tkinter import ttk, messagebox

from database import init_db, add_result, get_results
from osint_search import generate_profiles
from report import export_csv, export_json


class OSINTApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Social Media OSINT Tool")
        self.root.geometry("1000x600")

        init_db()

        self.create_widgets()
        self.load_database()

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="Social Media OSINT Tool",
            font=("Arial", 22, "bold")
        )
        title.pack(pady=15)

        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        tk.Label(
            input_frame,
            text="Public Username:"
        ).grid(row=0, column=0, padx=5)

        self.username_entry = tk.Entry(
            input_frame,
            width=35
        )
        self.username_entry.grid(row=0, column=1, padx=5)

        search_btn = tk.Button(
            input_frame,
            text="Generate Profiles",
            command=self.search_username
        )
        search_btn.grid(row=0, column=2, padx=5)

        # Table
        columns = (
            "id",
            "username",
            "platform",
            "url",
            "notes",
            "date"
        )

        self.tree = ttk.Treeview(
            self.root,
            columns=columns,
            show="headings"
        )

        self.tree.heading("id", text="ID")
        self.tree.heading("username", text="Username")
        self.tree.heading("platform", text="Platform")
        self.tree.heading("url", text="Public Profile URL")
        self.tree.heading("notes", text="Notes")
        self.tree.heading("date", text="Created")

        self.tree.column("id", width=50)
        self.tree.column("username", width=130)
        self.tree.column("platform", width=100)
        self.tree.column("url", width=300)
        self.tree.column("notes", width=180)
        self.tree.column("date", width=150)

        self.tree.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="Export CSV",
            command=self.export_csv_file,
            width=15
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="Export JSON",
            command=self.export_json_file,
            width=15
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame,
            text="Refresh",
            command=self.load_database,
            width=15
        ).grid(row=0, column=2, padx=5)

    def search_username(self):

        username = self.username_entry.get().strip()

        if not username:
            messagebox.showwarning(
                "Input Required",
                "Please enter a public username."
            )
            return

        profiles = generate_profiles(username)

        for profile in profiles:

            add_result(
                username=profile["username"],
                platform=profile["platform"],
                profile_url=profile["url"],
                notes="Public profile candidate"
            )

        self.load_database()

        messagebox.showinfo(
            "Completed",
            f"Generated {len(profiles)} public profile candidates."
        )

    def load_database(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        results = get_results()

        for row in results:
            self.tree.insert("", "end", values=row)

    def export_csv_file(self):

        filename = export_csv()

        messagebox.showinfo(
            "Export Complete",
            f"CSV report created:\n{filename}"
        )

    def export_json_file(self):

        filename = export_json()

        messagebox.showinfo(
            "Export Complete",
            f"JSON report created:\n{filename}"
        )


if __name__ == "__main__":

    root = tk.Tk()

    app = OSINTApp(root)

    root.mainloop()
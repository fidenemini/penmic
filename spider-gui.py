import zapv2
import time
import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.url_label = tk.Label(self, text="URL to scan:")
        self.url_label.pack()

        self.url_entry = tk.Entry(self)
        self.url_entry.pack()

        self.scan_button = tk.Button(self, text="Scan", command=self.scan)
        self.scan_button.pack()

        self.results = tk.Text(self, height=10, width=50)
        self.results.pack()

    def scan(self):
        target = self.url_entry.get()
        risks = [
            'A01:2021-Broken Access Control',
            'A02:2021-Cryptographic Failures',
            'A03:2021-Injection',
            'A04:2021-Insecure Direct Object References',
            'A05:2021-Security Misconfiguration',
            'A06:2021-Sensitive Data Exposure',
            'A07:2021-Missing Function Level Access Control',
            'A08:2021-Cross-Site Request Forgery (CSRF)',
            'A09:2021-Using Components with Known Vulnerabilities',
            'A10:2021-Insufficient Logging and Monitoring'
        ]
        zap = zapv2.ZAPv2(apikey='api-key')
        zap.spider.scan(target)
        while (int(zap.spider.status(target)) < 100):
            time.sleep(2)
        zap.ascan.scan(target)
        while (int(zap.ascan.status(target)) < 100):
            time.sleep(5)
        alerts = zap.core.alerts()
        self.results.delete(1.0, tk.END)
        for risk in risks:
            for alert in alerts:
                if risk in alert.get('name'):
                    self.results.insert(tk.END, 'Risk found: ' + risk + ' at URL: ' + alert.get('url') + '\n')
        zap.core.shutdown()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
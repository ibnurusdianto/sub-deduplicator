from rich.console import Console
from rich.progress import Progress
from rich.text import Text
import time

console = Console()

def remove_duplicates(input_file, output_file):
    unique_subdomains = []
    try:
        with open(input_file, 'r') as file:
            console.print(Text("Membaca subdomains dari {input_file}...", style="bold blue"))
            with Progress() as progress:
                task = progress.add_task("[cyan]Mengumpulkan subdomains unik...", total=1)

                for line in file:
                    subdomain = line.strip().lower()
                    if subdomain and subdomain not in unique_subdomains:
                        unique_subdomains.append(subdomain)
                
                progress.update(task, completed=1)

        console.print(Text(f"Total subdomains ditemukan: {len(unique_subdomains)}", style="bold green"))
        sorted_unique_subdomains = sorted(unique_subdomains)

        with open(output_file, 'w') as file:
            for subdomain in sorted_unique_subdomains:
                file.write(subdomain + '\n')
        
        console.print(Text(f"Hasil unik subdomains telah disimpan ke: {output_file}", style="bold green"))
        console.print(Text(f"Total subdomains unik: {len(sorted_unique_subdomains)}", style="bold green"))
    
    except FileNotFoundError:
        console.print(Text("Error: File tidak ditemukan.", style="bold red"))
    except Exception as e:
        console.print(Text(f"Terjadi kesalahan: {e}", style="bold red"))

def main():
    input_file = 'subdomains.txt'
    output_file = 'unique_subdomains.txt'
    remove_duplicates(input_file, output_file)

if __name__ == "__main__":
    main()

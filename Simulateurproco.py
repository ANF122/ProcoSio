import tkinter as tk
from tkinter import ttk, scrolledtext
import tkinter.font as tkFont

print("Starting imports...")  # Debug print

class AdvancedCPU:
    def __init__(self):
        print("Initializing AdvancedCPU...")  # Debug print
        self.registers = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        self.memory = [0] * 256
        self.pc = 0
        self.running = True
        self.output_text = None
        self.reg_display_var = None
        self.mem_display_var = None

    def load_program(self, program):
        print(f"Loading program: {program}")  # Debug print
        self.memory[:len(program)] = program
        self.pc = 0

    def fetch(self):
        if 0 <= self.pc < len(self.memory):
            instruction = self.memory[self.pc]
            self.pc += 1
            return instruction
        else:
            self.running = False
            self.log("Error: Program counter out of bounds.")
            return None

    def execute(self, instruction):
        print(f"Executing instruction: {instruction}")  # Debug print
        if instruction is None:
            return

        opcode, *operands = instruction
        try:
            if opcode == 1:  # MOV A, B
                self.registers[operands[0]] = self.registers[operands[1]]
            elif opcode == 2:  # ADD A, B
                self.registers[operands[0]] += self.registers[operands[1]]
            elif opcode == 3:  # SUB A, B
                self.registers[operands[0]] -= self.registers[operands[1]]
            elif opcode == 4:  # LOAD A, addr
                if 0 <= operands[1] < len(self.memory):
                    self.registers[operands[0]] = self.memory[operands[1]]
                else:
                    self.log(f"Error: Memory address {operands[1]} out of bounds.")
            elif opcode == 5:  # STORE A, addr
                if 0 <= operands[1] < len(self.memory):
                    self.memory[operands[1]] = self.registers[operands[0]]
                else:
                    self.log(f"Error: Memory address {operands[1]} out of bounds.")
            elif opcode == 6:  # JMP addr
                if 0 <= operands[0] < len(self.memory):
                    self.pc = operands[0]
                else:
                    self.log(f"Error: Jump address {operands[0]} out of bounds.")
            elif opcode == 7:  # CMP A, B
                result = "Equal" if self.registers[operands[0]] == self.registers[operands[1]] else "Not Equal"
                self.log(f"Compare {operands[0]}, {operands[1]}: {result}")
            elif opcode == 8:  # HALT
                self.running = False
                self.log("Program halted.")
            else:
                self.log(f"Error: Unknown instruction {opcode}.")
        except KeyError as e:
            self.log(f"Error: Invalid register {e}")
        except IndexError:
            self.log("Error: Insufficient operands for instruction.")

    def run(self):
        print("Running program...")  # Debug print
        while self.running:
            instruction = self.fetch()
            self.execute(instruction)
            self.update_display()

    def log(self, message):
        print(f"Log: {message}")  # Debug print
        if self.output_text:
            self.output_text.config(state='normal')
            self.output_text.insert(tk.END, message + "\n")
            self.output_text.see(tk.END)
            self.output_text.config(state='disabled')

    def update_display(self):
        if self.reg_display_var:
            self.reg_display_var.set(f"Registers: {self.registers}")
        if self.mem_display_var:
            self.mem_display_var.set(f"Memory (first 16 bytes): {self.memory[:16]}")

    def execute_command(self, command):
        print(f"Executing command: {command}")  # Debug print
        command = command.strip().lower()
        try:
            if command.startswith("load"):
                program = list(map(int, command.split()[1:]))
                self.load_program(program)
                self.log("Program loaded.")
            elif command == "exec":
                self.run()
            elif command == "status":
                self.update_display()
            elif command.startswith("setreg"):
                _, reg, value = command.split()
                if reg.upper() in self.registers:
                    self.registers[reg.upper()] = int(value)
                    self.update_display()
                    self.log(f"Register {reg.upper()} updated to {value}.")
                else:
                    self.log(f"Error: Invalid register {reg}")
            elif command.startswith("setmem"):
                _, addr, value = command.split()
                addr = int(addr)
                if 0 <= addr < len(self.memory):
                    self.memory[addr] = int(value)
                    self.update_display()
                    self.log(f"Memory at address {addr} updated to {value}.")
                else:
                    self.log(f"Error: Memory address {addr} out of bounds.")
            else:
                self.log("Error: Unrecognized command.")
        except Exception as e:
            self.log(f"Error: {str(e)}")

class CPUApp:
    def __init__(self, root):
        print("Initializing CPUApp...")  # Debug print
        self.root = root
        self.root.title("CPU Simulator")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')

        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.cpu = AdvancedCPU()

        self.create_widgets()
        self.layout_widgets()

        self.cpu.output_text = self.output_text
        self.cpu.reg_display_var = self.reg_display_var
        self.cpu.mem_display_var = self.mem_display_var

    def create_widgets(self):
        print("Creating widgets...")  # Debug print
        title_font = tkFont.Font(family="Helvetica", size=16, weight="bold")
        
        self.info_frame = ttk.Frame(self.root, padding="10")
        
        self.reg_title = ttk.Label(self.info_frame, text="Registers", font=title_font)
        
        self.reg_display_var = tk.StringVar()
        self.reg_display_var.set("A: 0, B: 0, C: 0, D: 0")
        self.reg_display = ttk.Label(self.info_frame, textvariable=self.reg_display_var, 
                                     background='white', padding=5, relief='sunken')

        self.mem_title = ttk.Label(self.info_frame, text="Memory (first 16 bytes)", font=title_font)
        
        self.mem_display_var = tk.StringVar()
        self.mem_display_var.set("0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0")
        self.mem_display = ttk.Label(self.info_frame, textvariable=self.mem_display_var, 
                                     background='white', padding=5, relief='sunken')

        self.output_frame = ttk.Frame(self.root, padding="10")
        self.output_title = ttk.Label(self.output_frame, text="Output Log", font=title_font)
        self.output_text = scrolledtext.ScrolledText(self.output_frame, width=70, height=15)
        self.output_text.config(state='disabled')

        self.input_frame = ttk.Frame(self.root, padding="10")
        self.command_label = ttk.Label(self.input_frame, text="Enter command:")
        self.command_entry = ttk.Entry(self.input_frame, width=50)
        self.command_entry.bind('<Return>', self.execute_command)

        self.execute_button = ttk.Button(self.input_frame, text="Execute", command=self.execute_command)

    def layout_widgets(self):
        print("Laying out widgets...")  # Debug print
        self.info_frame.pack(fill='x', padx=10, pady=10)
        self.reg_title.pack(anchor='w')
        self.reg_display.pack(fill='x', pady=(0, 10))
        self.mem_title.pack(anchor='w')
        self.mem_display.pack(fill='x')

        self.output_frame.pack(fill='both', expand=True, padx=10, pady=10)
        self.output_title.pack(anchor='w')
        self.output_text.pack(fill='both', expand=True)

        self.input_frame.pack(fill='x', padx=10, pady=10)
        self.command_label.pack(side='left', padx=(0, 10))
        self.command_entry.pack(side='left', expand=True, fill='x')
        self.execute_button.pack(side='left', padx=(10, 0))

    def execute_command(self, event=None):
        command = self.command_entry.get()
        self.cpu.execute_command(command)
        self.command_entry.delete(0, tk.END)

def main():
    print("Starting main function...")  # Debug print
    root = tk.Tk()
    print("Tk instance created")  # Debug print
    app = CPUApp(root)
    print("CPUApp instance created")  # Debug print
    root.mainloop()
    print("Mainloop started")  # Debug print

if __name__ == "__main__":
    main()
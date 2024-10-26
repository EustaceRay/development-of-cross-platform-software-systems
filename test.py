import subprocess
import time

def process(command):
    return subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        universal_newlines=True,
        shell=True
    )

def expect(proc, pattern, timeout=5):
    pattern = pattern.strip("\n")
    buffer = ""
    start_time = time.time()

    while True:
        if time.time() - start_time > timeout:
            print(f"Timeout while waiting for: {pattern}")
            return False

        char = proc.stdout.read(1)
        if not char:
            break

        buffer += char

        if buffer.endswith(pattern):
            return True

    return False

def expect_lines(proc, lines, timeout=10):
    for line in lines:
        if not expect(proc, line, timeout=timeout):
            print(f"Failed to match line: {line}")
            return False
    return True

def write(proc, text):
    proc.stdin.write(f'{text}\n')
    proc.stdin.flush()
    return text

def test():
    print("Launching processes")
    try:
        py = process('python pasart.py')
        bas = process('pasart.bas')

        expected_greetings = '''
                        PASART
                  CREATIVE COMPUTING
                MORRISTOWN   NEW JERSEY



THIS PROGRAM CREATES ARTIST DESIGNS BASED ON PASCAL'S TRIANGLE.
YOU HAVE 3 BASIC TYPES OF DESIGNS TO SELECT FROM:
1. A SINGLE PASCAL'S TRIANGLE (PLAYED WITH AN ARTISTIC FLARE)
2. TWO 'ARTSY' PASCAL'S TRIANGLES PRINTED BACK TO BACK
3. FOUR 'ARTSY' TRIANGLES IN THE CORNER OF
   A SQUARE ARRAY.
WHAT'S YOUR PLEASURE? 1, 2 OR 3? 
'''
        print("expecting greetings...")
        if not (expect(py, expected_greetings) and expect(bas, expected_greetings)):
            print("Failed to match greetings")
            return

        print("[+] TEST 1 - PASSED")

        print("sending choice...")
        write(py, '1')
        write(bas, '1')
        print("[+] KEYS SENT")

        multiples_prompt = "WHICH MULTIPLES DO YOU WANT REPRESENTED WITH BLANKS? "
        if not (expect(py, multiples_prompt) and expect(bas, multiples_prompt)):
            print("Failed to match multiples prompt")
            return

        print("[+] TEST 2 - PASSED")

        print("sending multiples...")
        write(py, '3')
        write(bas, '3')
        print("[+] KEYS SENT")

        size_prompt = "HOW MANY ROWS AND COLUMS IN THE ARRAY (36 IS MAXIMUM)? "
        if not expect(py, size_prompt) or not expect(bas, size_prompt):
            print("Failed to match size prompt")
            return

        print("[+] TEST 3 - PASSED")

        print("sending size...")
        write(py, '5')
        write(bas, '5')
        print("[+] KEYS SENT")

        final_output_lines = [
            "* * * * *",
            "* *   * *",
            "*     *",
            "* * * * *",
            "* *   * *"
        ]

        if not expect_lines(py, final_output_lines) or not expect_lines(bas, final_output_lines):
            print("Failed to match final output")
            return

        print("[+] FINAL TEST - PASSED")

    except Exception as ex:
        print(f"Error: {ex}")

test()

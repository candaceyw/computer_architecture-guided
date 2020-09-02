#
# convert ob11001010 to decimal
# answer: 202
#
# conver 115 to binary
# Answer: 0b01110011
# convert 54 to binary (try making it 8 bit)
#   Answer: 0b00110110
#     convert 54 to hex
# 0x36

import sys

# operation codes
# OP codes
PRINT_HELLO_WORLD = 1  # 0b00000001
HALT              = 2  # 0b00000010
PRINT_NUM         = 3  # 0b00000011
SAVE_REG          = 4
PRINT_REG         = 5
ADD               = 6

memory = [
    SAVE_REG,
    2,
    1,
    SAVE_REG,
    2,
    2,
    ADD,
    1,
    2,
    PRINT_REG,
    1,
    HALT
]

registers = [0] * 8

running = True

pc = 0  # program counter

while running:
    # read line by line from memory
    instruction = memory[pc]

    if instruction == PRINT_HELLO_WORLD:
        # print Hello world
        # move the PC up 1 to the next instruction
        print("Hello World")
        pc += 1

    elif instruction == PRINT_NUM:
        # print the number in the NEXT memory slot
        num = memory[pc + 1]
        print(num)
        pc += 2

    elif instruction == SAVE_REG:
        # save some value to some register
        # first number after instruction will be the Value to store
        # second number after instruction will be register
        num = memory[pc + 1]
        reg_location = memory[pc + 2]
        registers[reg_location] = num
        pc += 3

    elif instruction == PRINT_REG:
        reg_location = memory[pc + 1]
        print(registers[reg_location])
        pc += 2

    elif instruction == ADD:
        # ADD takes TWO registers, adds their values
        # and stores the result in the first register given
        # Get register 1
        # Get register 23
        # add the values of both registers together
        # stores in register 1
        reg_1 = memory[pc + 1]
        reg_2 = memory[pc + 2]
        registers[reg_1] += registers[reg_2]
        pc += 3

    elif instruction == HALT:
        running = False
        pc +=1

    else:
        print(f"Unknown instruction {instruction}")
        sys.exit(1)

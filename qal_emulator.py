import sys
from semantic_register import SemanticRegister
from meaning_cache import MeaningCache
from instruction_decoder import decode
from execution_engine import execute
from global_semantic_field import global_semantic_field

def run(program_path):
    registers = {}
    cache = MeaningCache()

    with open(program_path, "r") as f:
        lines = f.readlines()

    print(f'Running "{program_path}"...\n')

    for line in lines:
        if not line.strip() or line.startswith("#"):
            continue

        op, args = decode(line)
        gsf = global_semantic_field(registers)
        execute(op, args, registers, cache, gsf)

        print(f"{op} -> {registers}")

if __name__ == "__main__":
    run(sys.argv[1])

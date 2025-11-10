import os
import sys


# Make sure the 'tests' folder is on the path
sys.path.append("./")

flags = []

def run_tests():
    for f in os.listdir("tests"):
        if f.startswith("test_") and f.endswith(".py"):
            module_name = f[:-3]
            mod = __import__(module_name)
            if hasattr(mod, "run"):
                print("\n=== Running", module_name, "===")
                flags.append(mod.run())
    print("\n=== Test Summary ===")
    for test_flags in flags:
        for test_name, result in test_flags:
            status = "PASS" if result else "FAIL"
            print(f"{test_name}: {status}")
    correct_results = sum(1 for name, val in test_flags if val is True)
    wrong_results = sum(1 for name, val in test_flags if val is False)
    print("Correct result/s: ",correct_results)
    print("Wrong result/s:",wrong_results)
    sys.exit(1) if wrong_results > 0 else sys.exit(0)
                

if __name__ == "__main__":
    run_tests()
import cx_Freeze

executables = [cx_Freeze.Executable("green_defender.py")]

cx_Freeze.setup(
	name="Green Defender",
	options={"build_exe": {"packages":["pygame"],
							"include_files":["images/",
											"sounds/",
											"high_score.txt"]}},
	executables = executables
	)
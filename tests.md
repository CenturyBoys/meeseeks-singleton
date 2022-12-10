```bash
2022-12-10 10:50:32,864: Running clean trial
============================= test session starts ==============================
platform linux -- Python 3.8.10, pytest-7.2.0, pluggy-1.0.0
rootdir: /home/devv/projects/meeseeks
plugins: cov-4.0.0
collected 40 items

tests/test_iam.py .............                                          [ 32%]
tests/test_iam_configs.py ................                               [ 72%]
tests/test_iam_global_vs_single.py .....                                 [ 85%]
tests/hash/test_iam_hash_generator.py ......                             [100%]

---------- coverage: platform linux, python 3.8.10-final-0 -----------
Name                                        Stmts   Miss  Cover   Missing
-------------------------------------------------------------------------
meeseeks/__init__.py                            1      0   100%
meeseeks/iam.py                               117      0   100%
meeseeks/src/__init__.py                        0      0   100%
meeseeks/src/hash/__init__.py                   0      0   100%
meeseeks/src/hash/args_and_kwargs_hash.py       7      0   100%
-------------------------------------------------------------------------
TOTAL                                         125      0   100%


============================== 40 passed in 2.23s ==============================
2022-12-10 10:50:35,377: [92m33 mutation targets found in meeseeks/iam.py AST.[0m
2022-12-10 10:50:35,378: [93m0 mutation targets found in meeseeks/__init__.py AST.[0m
2022-12-10 10:50:35,378: [93m0 mutation targets found in meeseeks/src/__init__.py AST.[0m
2022-12-10 10:50:35,378: [93m0 mutation targets found in meeseeks/src/hash/__init__.py AST.[0m
2022-12-10 10:50:35,378: [93m0 mutation targets found in meeseeks/src/hash/args_and_kwargs_hash.py AST.[0m
2022-12-10 10:50:35,378: Setting random.seed to: None
2022-12-10 10:50:35,383: Total sample space size: 33
2022-12-10 10:50:35,383: [93m40 exceeds sample space, using full sample: 33.[0m
2022-12-10 10:50:35,383: Starting individual mutation trials!
2022-12-10 10:50:35,383: Running serial (single processor) dispatch mode.
2022-12-10 10:50:35,383: Current target location: iam.py, LocIndex(ast_class='NameConstant', lineno=8, col_offset=35, op_type=False, end_lineno=8, end_col_offset=40)
2022-12-10 10:50:37,929: [91mResult: Survived at meeseeks/iam.py: (8, 35)[0m
2022-12-10 10:50:37,929: [91mBreak on survival: stopping further mutations at location.[0m
2022-12-10 10:50:37,929: Current target location: iam.py, LocIndex(ast_class='NameConstant', lineno=15, col_offset=53, op_type=None, end_lineno=15, end_col_offset=57)
2022-12-10 10:50:40,668: [91mResult: Survived at meeseeks/iam.py: (15, 53)[0m
2022-12-10 10:50:40,669: [91mBreak on survival: stopping further mutations at location.[0m
2022-12-10 10:50:40,669: Current target location: iam.py, LocIndex(ast_class='NameConstant', lineno=15, col_offset=70, op_type=None, end_lineno=15, end_col_offset=74)
2022-12-10 10:50:43,224: [92mResult: Detected at meeseeks/iam.py: (15, 70)[0m
2022-12-10 10:50:45,667: [91mResult: Survived at meeseeks/iam.py: (15, 70)[0m
2022-12-10 10:50:45,667: [91mBreak on survival: stopping further mutations at location.[0m
2022-12-10 10:50:45,667: Current target location: iam.py, LocIndex(ast_class='NameConstant', lineno=31, col_offset=44, op_type=None, end_lineno=31, end_col_offset=48)
2022-12-10 10:50:48,331: [91mResult: Survived at meeseeks/iam.py: (31, 44)[0m
2022-12-10 10:50:48,331: [91mBreak on survival: stopping further mutations at location.[0m
2022-12-10 10:50:48,331: Current target location: iam.py, LocIndex(ast_class='NameConstant', lineno=31, col_offset=61, op_type=None, end_lineno=31, end_col_offset=65)
2022-12-10 10:50:50,964: [92mResult: Detected at meeseeks/iam.py: (31, 61)[0m
2022-12-10 10:50:53,478: [91mResult: Survived at meeseeks/iam.py: (31, 61)[0m
2022-12-10 10:50:53,478: [91mBreak on survival: stopping further mutations at location.[0m
2022-12-10 10:50:53,479: Current target location: iam.py, LocIndex(ast_class='If', lineno=52, col_offset=8, op_type='If_Statement', end_lineno=53, end_col_offset=32)
2022-12-10 10:50:55,987: [92mResult: Detected at meeseeks/iam.py: (52, 8)[0m
2022-12-10 10:50:57,719: [92mResult: Detected at meeseeks/iam.py: (52, 8)[0m
2022-12-10 10:50:57,719: Current target location: iam.py, LocIndex(ast_class='CompareIs', lineno=52, col_offset=11, op_type=<class '_ast.Is'>, end_lineno=52, end_col_offset=31)
2022-12-10 10:50:59,426: [92mResult: Detected at meeseeks/iam.py: (52, 11)[0m
2022-12-10 10:50:59,426: Current target location: iam.py, LocIndex(ast_class='NameConstant', lineno=52, col_offset=27, op_type=None, end_lineno=52, end_col_offset=31)
2022-12-10 10:51:01,061: [92mResult: Detected at meeseeks/iam.py: (52, 27)[0m
2022-12-10 10:51:02,653: [92mResult: Detected at meeseeks/iam.py: (52, 27)[0m
2022-12-10 10:51:02,654: Current target location: iam.py, LocIndex(ast_class='NameConstant', lineno=53, col_offset=27, op_type=False, end_lineno=53, end_col_offset=32)
2022-12-10 10:51:04,573: [92mResult: Detected at meeseeks/iam.py: (53, 27)[0m
2022-12-10 10:51:07,214: [92mResult: Detected at meeseeks/iam.py: (53, 27)[0m
2022-12-10 10:51:07,214: Current target location: iam.py, LocIndex(ast_class='If', lineno=54, col_offset=8, op_type='If_Statement', end_lineno=55, end_col_offset=19)
2022-12-10 10:51:09,980: [92mResult: Detected at meeseeks/iam.py: (54, 8)[0m
2022-12-10 10:51:12,852: [92mResult: Detected at meeseeks/iam.py: (54, 8)[0m
2022-12-10 10:51:12,852: Current target location: iam.py, LocIndex(ast_class='CompareIs', lineno=54, col_offset=11, op_type=<class '_ast.Is'>, end_lineno=54, end_col_offset=22)
2022-12-10 10:51:15,779: [92mResult: Detected at meeseeks/iam.py: (54, 11)[0m
2022-12-10 10:51:15,779: Current target location: iam.py, LocIndex(ast_class='NameConstant', lineno=54, col_offset=18, op_type=None, end_lineno=54, end_col_offset=22)
2022-12-10 10:51:18,763: [92mResult: Detected at meeseeks/iam.py: (54, 18)[0m
2022-12-10 10:51:21,835: [92mResult: Detected at meeseeks/iam.py: (54, 18)[0m
2022-12-10 10:51:21,836: Current target location: iam.py, LocIndex(ast_class='If', lineno=57, col_offset=8, op_type='If_Statement', end_lineno=61, end_col_offset=13)
2022-12-10 10:51:24,382: [92mResult: Detected at meeseeks/iam.py: (57, 8)[0m
2022-12-10 10:51:25,448: [92mResult: Detected at meeseeks/iam.py: (57, 8)[0m
2022-12-10 10:51:25,448: Current target location: iam.py, LocIndex(ast_class='BoolOp', lineno=57, col_offset=11, op_type=<class '_ast.Or'>, end_lineno=57, end_col_offset=73)
2022-12-10 10:51:28,129: [92mResult: Detected at meeseeks/iam.py: (57, 11)[0m
2022-12-10 10:51:28,130: Current target location: iam.py, LocIndex(ast_class='If', lineno=99, col_offset=8, op_type='If_Statement', end_lineno=111, end_col_offset=31)
2022-12-10 10:51:28,645: [92mResult: Detected at meeseeks/iam.py: (99, 8)[0m
2022-12-10 10:51:29,172: [92mResult: Detected at meeseeks/iam.py: (99, 8)[0m
2022-12-10 10:51:29,172: Current target location: iam.py, LocIndex(ast_class='If', lineno=102, col_offset=12, op_type='If_Statement', end_lineno=111, end_col_offset=31)
2022-12-10 10:51:29,658: [92mResult: Detected at meeseeks/iam.py: (102, 12)[0m
2022-12-10 10:51:32,115: [92mResult: Detected at meeseeks/iam.py: (102, 12)[0m
2022-12-10 10:51:32,115: Current target location: iam.py, LocIndex(ast_class='If', lineno=128, col_offset=12, op_type='If_Statement', end_lineno=147, end_col_offset=17)
2022-12-10 10:51:34,765: [92mResult: Detected at meeseeks/iam.py: (128, 12)[0m
2022-12-10 10:51:37,809: [92mResult: Detected at meeseeks/iam.py: (128, 12)[0m
2022-12-10 10:51:37,809: Current target location: iam.py, LocIndex(ast_class='If', lineno=129, col_offset=16, op_type='If_Statement', end_lineno=132, end_col_offset=42)
2022-12-10 10:51:40,483: [92mResult: Detected at meeseeks/iam.py: (129, 16)[0m
2022-12-10 10:51:42,324: [92mResult: Detected at meeseeks/iam.py: (129, 16)[0m
2022-12-10 10:51:42,325: Current target location: iam.py, LocIndex(ast_class='If', lineno=140, col_offset=16, op_type='If_Statement', end_lineno=143, end_col_offset=42)
2022-12-10 10:51:45,108: [92mResult: Detected at meeseeks/iam.py: (140, 16)[0m
2022-12-10 10:51:46,884: [92mResult: Detected at meeseeks/iam.py: (140, 16)[0m
2022-12-10 10:51:46,884: Current target location: iam.py, LocIndex(ast_class='If', lineno=176, col_offset=8, op_type='If_Statement', end_lineno=177, end_col_offset=64)
2022-12-10 10:51:48,986: [92mResult: Detected at meeseeks/iam.py: (176, 8)[0m
2022-12-10 10:51:51,594: [92mResult: Detected at meeseeks/iam.py: (176, 8)[0m
2022-12-10 10:51:51,594: Current target location: iam.py, LocIndex(ast_class='CompareIs', lineno=176, col_offset=11, op_type=<class '_ast.Is'>, end_lineno=176, end_col_offset=58)
2022-12-10 10:51:53,393: [92mResult: Detected at meeseeks/iam.py: (176, 11)[0m
2022-12-10 10:51:53,393: Current target location: iam.py, LocIndex(ast_class='NameConstant', lineno=176, col_offset=54, op_type=None, end_lineno=176, end_col_offset=58)
2022-12-10 10:51:55,300: [92mResult: Detected at meeseeks/iam.py: (176, 54)[0m
2022-12-10 10:51:57,278: [92mResult: Detected at meeseeks/iam.py: (176, 54)[0m
2022-12-10 10:51:57,279: Current target location: iam.py, LocIndex(ast_class='If', lineno=210, col_offset=8, op_type='If_Statement', end_lineno=218, end_col_offset=52)
2022-12-10 10:52:00,038: [92mResult: Detected at meeseeks/iam.py: (210, 8)[0m
2022-12-10 10:52:01,683: [92mResult: Detected at meeseeks/iam.py: (210, 8)[0m
2022-12-10 10:52:01,683: Current target location: iam.py, LocIndex(ast_class='If', lineno=211, col_offset=12, op_type='If_Statement', end_lineno=218, end_col_offset=52)
2022-12-10 10:52:03,454: [92mResult: Detected at meeseeks/iam.py: (211, 12)[0m
2022-12-10 10:52:05,914: [92mResult: Detected at meeseeks/iam.py: (211, 12)[0m
2022-12-10 10:52:05,915: Current target location: iam.py, LocIndex(ast_class='If', lineno=212, col_offset=16, op_type='If_Statement', end_lineno=218, end_col_offset=52)
2022-12-10 10:52:08,444: [92mResult: Detected at meeseeks/iam.py: (212, 16)[0m
2022-12-10 10:52:10,847: [92mResult: Detected at meeseeks/iam.py: (212, 16)[0m
2022-12-10 10:52:10,848: Current target location: iam.py, LocIndex(ast_class='BinOp', lineno=213, col_offset=34, op_type=<class '_ast.Add'>, end_lineno=213, end_col_offset=74)
2022-12-10 10:52:13,253: [92mResult: Detected at meeseeks/iam.py: (213, 34)[0m
2022-12-10 10:52:15,636: [92mResult: Detected at meeseeks/iam.py: (213, 34)[0m
2022-12-10 10:52:18,118: [92mResult: Detected at meeseeks/iam.py: (213, 34)[0m
2022-12-10 10:52:20,580: [92mResult: Detected at meeseeks/iam.py: (213, 34)[0m
2022-12-10 10:52:22,975: [92mResult: Detected at meeseeks/iam.py: (213, 34)[0m
2022-12-10 10:52:25,530: [92mResult: Detected at meeseeks/iam.py: (213, 34)[0m
2022-12-10 10:52:25,530: Current target location: iam.py, LocIndex(ast_class='If', lineno=214, col_offset=20, op_type='If_Statement', end_lineno=215, end_col_offset=56)
2022-12-10 10:52:27,961: [92mResult: Detected at meeseeks/iam.py: (214, 20)[0m
2022-12-10 10:52:30,393: [92mResult: Detected at meeseeks/iam.py: (214, 20)[0m
2022-12-10 10:52:30,393: Current target location: iam.py, LocIndex(ast_class='Compare', lineno=214, col_offset=23, op_type=<class '_ast.GtE'>, end_lineno=214, end_col_offset=67)
2022-12-10 10:52:32,901: [92mResult: Detected at meeseeks/iam.py: (214, 23)[0m
2022-12-10 10:52:35,356: [92mResult: Detected at meeseeks/iam.py: (214, 23)[0m
2022-12-10 10:52:37,934: [92mResult: Detected at meeseeks/iam.py: (214, 23)[0m
2022-12-10 10:52:40,573: [92mResult: Detected at meeseeks/iam.py: (214, 23)[0m
2022-12-10 10:52:43,075: [92mResult: Detected at meeseeks/iam.py: (214, 23)[0m
2022-12-10 10:52:43,075: Current target location: iam.py, LocIndex(ast_class='If', lineno=265, col_offset=8, op_type='If_Statement', end_lineno=272, end_col_offset=48)
2022-12-10 10:52:45,065: [92mResult: Detected at meeseeks/iam.py: (265, 8)[0m
2022-12-10 10:52:48,029: [92mResult: Detected at meeseeks/iam.py: (265, 8)[0m
2022-12-10 10:52:48,029: Current target location: iam.py, LocIndex(ast_class='If', lineno=266, col_offset=12, op_type='If_Statement', end_lineno=272, end_col_offset=48)
2022-12-10 10:52:50,896: [92mResult: Detected at meeseeks/iam.py: (266, 12)[0m
2022-12-10 10:52:53,637: [92mResult: Detected at meeseeks/iam.py: (266, 12)[0m
2022-12-10 10:52:53,637: Current target location: iam.py, LocIndex(ast_class='BinOp', lineno=267, col_offset=30, op_type=<class '_ast.Add'>, end_lineno=267, end_col_offset=70)
2022-12-10 10:52:56,339: [92mResult: Detected at meeseeks/iam.py: (267, 30)[0m
2022-12-10 10:52:59,060: [92mResult: Detected at meeseeks/iam.py: (267, 30)[0m
2022-12-10 10:53:01,520: [92mResult: Detected at meeseeks/iam.py: (267, 30)[0m
2022-12-10 10:53:03,945: [92mResult: Detected at meeseeks/iam.py: (267, 30)[0m
2022-12-10 10:53:06,486: [92mResult: Detected at meeseeks/iam.py: (267, 30)[0m
2022-12-10 10:53:09,181: [92mResult: Detected at meeseeks/iam.py: (267, 30)[0m
2022-12-10 10:53:09,181: Current target location: iam.py, LocIndex(ast_class='If', lineno=268, col_offset=16, op_type='If_Statement', end_lineno=269, end_col_offset=52)
2022-12-10 10:53:11,587: [92mResult: Detected at meeseeks/iam.py: (268, 16)[0m
2022-12-10 10:53:13,994: [92mResult: Detected at meeseeks/iam.py: (268, 16)[0m
2022-12-10 10:53:13,994: Current target location: iam.py, LocIndex(ast_class='Compare', lineno=268, col_offset=19, op_type=<class '_ast.GtE'>, end_lineno=268, end_col_offset=63)
2022-12-10 10:53:16,411: [92mResult: Detected at meeseeks/iam.py: (268, 19)[0m
2022-12-10 10:53:18,830: [92mResult: Detected at meeseeks/iam.py: (268, 19)[0m
2022-12-10 10:53:21,270: [92mResult: Detected at meeseeks/iam.py: (268, 19)[0m
2022-12-10 10:53:23,805: [92mResult: Detected at meeseeks/iam.py: (268, 19)[0m
2022-12-10 10:53:26,498: [92mResult: Detected at meeseeks/iam.py: (268, 19)[0m
2022-12-10 10:53:26,500: Running clean trial
============================= test session starts ==============================
platform linux -- Python 3.8.10, pytest-7.2.0, pluggy-1.0.0
rootdir: /home/devv/projects/meeseeks
plugins: cov-4.0.0
collected 40 items

tests/test_iam.py .............                                          [ 32%]
tests/test_iam_configs.py ................                               [ 72%]
tests/test_iam_global_vs_single.py .....                                 [ 85%]
tests/hash/test_iam_hash_generator.py ......                             [100%]

---------- coverage: platform linux, python 3.8.10-final-0 -----------
Name                                        Stmts   Miss  Cover   Missing
-------------------------------------------------------------------------
meeseeks/__init__.py                            1      0   100%
meeseeks/iam.py                               117      0   100%
meeseeks/src/__init__.py                        0      0   100%
meeseeks/src/hash/__init__.py                   0      0   100%
meeseeks/src/hash/args_and_kwargs_hash.py       7      0   100%
-------------------------------------------------------------------------
TOTAL                                         125      0   100%


============================== 40 passed in 2.29s ==============================
2022-12-10 10:53:29,188: CLI Report:

Mutatest diagnostic summary
===========================
 - Source location: /home/devv/projects/meeseeks/meeseeks
 - Test commands: ['pytest', '--cov=meeseeks', '--cov-report', 'term-missing']
 - Mode: s
 - Excluded files: []
 - N locations input: 40
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 33
 - Total locations identified: 33
 - Location sample coverage: 100.00 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:02.508962
 - Clean trial 2 run time: 0:00:02.685897
 - Mutation trials total run time: 0:02:51.125573

2022-12-10 10:53:29,188: Trial Summary Report:

Overall mutation trial summary
==============================
 - SURVIVED: 5
 - DETECTED: 68
 - TOTAL RUNS: 73
 - RUN DATETIME: 2022-12-10 10:53:29.187217

2022-12-10 10:53:29,188: Detected mutations:[92m

DETECTED
--------
 - meeseeks/iam.py: (l: 15, c: 70) - mutation from None to True
 - meeseeks/iam.py: (l: 31, c: 61) - mutation from None to True
 - meeseeks/iam.py: (l: 52, c: 8) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 52, c: 8) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 52, c: 11) - mutation from <class '_ast.Is'> to <class '_ast.IsNot'>
 - meeseeks/iam.py: (l: 52, c: 27) - mutation from None to False
 - meeseeks/iam.py: (l: 52, c: 27) - mutation from None to True
 - meeseeks/iam.py: (l: 53, c: 27) - mutation from False to None
 - meeseeks/iam.py: (l: 53, c: 27) - mutation from False to True
 - meeseeks/iam.py: (l: 54, c: 8) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 54, c: 8) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 54, c: 11) - mutation from <class '_ast.Is'> to <class '_ast.IsNot'>
 - meeseeks/iam.py: (l: 54, c: 18) - mutation from None to True
 - meeseeks/iam.py: (l: 54, c: 18) - mutation from None to False
 - meeseeks/iam.py: (l: 57, c: 8) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 57, c: 8) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 57, c: 11) - mutation from <class '_ast.Or'> to <class '_ast.And'>
 - meeseeks/iam.py: (l: 99, c: 8) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 99, c: 8) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 102, c: 12) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 102, c: 12) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 128, c: 12) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 128, c: 12) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 129, c: 16) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 129, c: 16) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 140, c: 16) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 140, c: 16) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 176, c: 8) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 176, c: 8) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 176, c: 11) - mutation from <class '_ast.Is'> to <class '_ast.IsNot'>
 - meeseeks/iam.py: (l: 176, c: 54) - mutation from None to False
 - meeseeks/iam.py: (l: 176, c: 54) - mutation from None to True
 - meeseeks/iam.py: (l: 210, c: 8) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 210, c: 8) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 211, c: 12) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 211, c: 12) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 212, c: 16) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 212, c: 16) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 213, c: 34) - mutation from <class '_ast.Add'> to <class '_ast.Pow'>
 - meeseeks/iam.py: (l: 213, c: 34) - mutation from <class '_ast.Add'> to <class '_ast.Mult'>
 - meeseeks/iam.py: (l: 213, c: 34) - mutation from <class '_ast.Add'> to <class '_ast.Div'>
 - meeseeks/iam.py: (l: 213, c: 34) - mutation from <class '_ast.Add'> to <class '_ast.Sub'>
 - meeseeks/iam.py: (l: 213, c: 34) - mutation from <class '_ast.Add'> to <class '_ast.FloorDiv'>
 - meeseeks/iam.py: (l: 213, c: 34) - mutation from <class '_ast.Add'> to <class '_ast.Mod'>
 - meeseeks/iam.py: (l: 214, c: 20) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 214, c: 20) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 214, c: 23) - mutation from <class '_ast.GtE'> to <class '_ast.Gt'>
 - meeseeks/iam.py: (l: 214, c: 23) - mutation from <class '_ast.GtE'> to <class '_ast.LtE'>
 - meeseeks/iam.py: (l: 214, c: 23) - mutation from <class '_ast.GtE'> to <class '_ast.Lt'>
 - meeseeks/iam.py: (l: 214, c: 23) - mutation from <class '_ast.GtE'> to <class '_ast.Eq'>
 - meeseeks/iam.py: (l: 214, c: 23) - mutation from <class '_ast.GtE'> to <class '_ast.NotEq'>
 - meeseeks/iam.py: (l: 265, c: 8) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 265, c: 8) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 266, c: 12) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 266, c: 12) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 267, c: 30) - mutation from <class '_ast.Add'> to <class '_ast.Mod'>
 - meeseeks/iam.py: (l: 267, c: 30) - mutation from <class '_ast.Add'> to <class '_ast.Sub'>
 - meeseeks/iam.py: (l: 267, c: 30) - mutation from <class '_ast.Add'> to <class '_ast.Div'>
 - meeseeks/iam.py: (l: 267, c: 30) - mutation from <class '_ast.Add'> to <class '_ast.Pow'>
 - meeseeks/iam.py: (l: 267, c: 30) - mutation from <class '_ast.Add'> to <class '_ast.FloorDiv'>
 - meeseeks/iam.py: (l: 267, c: 30) - mutation from <class '_ast.Add'> to <class '_ast.Mult'>
 - meeseeks/iam.py: (l: 268, c: 16) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 268, c: 16) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 268, c: 19) - mutation from <class '_ast.GtE'> to <class '_ast.Lt'>
 - meeseeks/iam.py: (l: 268, c: 19) - mutation from <class '_ast.GtE'> to <class '_ast.LtE'>
 - meeseeks/iam.py: (l: 268, c: 19) - mutation from <class '_ast.GtE'> to <class '_ast.Eq'>
 - meeseeks/iam.py: (l: 268, c: 19) - mutation from <class '_ast.GtE'> to <class '_ast.NotEq'>
 - meeseeks/iam.py: (l: 268, c: 19) - mutation from <class '_ast.GtE'> to <class '_ast.Gt'>[0m

2022-12-10 10:53:29,188: Timedout mutations:

2022-12-10 10:53:29,188: Surviving mutations:[91m

SURVIVED
--------
 - meeseeks/iam.py: (l: 8, c: 35) - mutation from False to None
 - meeseeks/iam.py: (l: 15, c: 53) - mutation from None to False
 - meeseeks/iam.py: (l: 15, c: 70) - mutation from None to False
 - meeseeks/iam.py: (l: 31, c: 44) - mutation from None to False
 - meeseeks/iam.py: (l: 31, c: 61) - mutation from None to False[0m

```

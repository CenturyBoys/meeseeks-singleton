```bash
2022-12-14 20:32:21,637: Running clean trial
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
meeseeks/iam.py                               119      0   100%
meeseeks/src/__init__.py                        0      0   100%
meeseeks/src/hash/__init__.py                   0      0   100%
meeseeks/src/hash/args_and_kwargs_hash.py       7      0   100%
-------------------------------------------------------------------------
TOTAL                                         127      0   100%


============================== 40 passed in 2.28s ==============================
2022-12-14 20:32:24,319: [92m33 mutation targets found in meeseeks/iam.py AST.[0m
2022-12-14 20:32:24,319: [93m0 mutation targets found in meeseeks/__init__.py AST.[0m
2022-12-14 20:32:24,320: [93m0 mutation targets found in meeseeks/src/__init__.py AST.[0m
2022-12-14 20:32:24,321: [93m0 mutation targets found in meeseeks/src/hash/__init__.py AST.[0m
2022-12-14 20:32:24,322: [93m0 mutation targets found in meeseeks/src/hash/args_and_kwargs_hash.py AST.[0m
2022-12-14 20:32:24,323: Setting random.seed to: None
2022-12-14 20:32:24,345: Total sample space size: 33
2022-12-14 20:32:24,345: [93m40 exceeds sample space, using full sample: 33.[0m
2022-12-14 20:32:24,345: Starting individual mutation trials!
2022-12-14 20:32:24,346: Running serial (single processor) dispatch mode.
2022-12-14 20:32:24,346: Current target location: iam.py, LocIndex(ast_class='NameConstant', lineno=10, col_offset=35, op_type=False, end_lineno=10, end_col_offset=40)
2022-12-14 20:32:27,327: [91mResult: Survived at meeseeks/iam.py: (10, 35)[0m
2022-12-14 20:32:27,327: [91mBreak on survival: stopping further mutations at location.[0m
2022-12-14 20:32:27,327: Current target location: iam.py, LocIndex(ast_class='NameConstant', lineno=17, col_offset=53, op_type=None, end_lineno=17, end_col_offset=57)
2022-12-14 20:32:29,971: [92mResult: Detected at meeseeks/iam.py: (17, 53)[0m
2022-12-14 20:32:32,503: [91mResult: Survived at meeseeks/iam.py: (17, 53)[0m
2022-12-14 20:32:32,503: [91mBreak on survival: stopping further mutations at location.[0m
2022-12-14 20:32:32,503: Current target location: iam.py, LocIndex(ast_class='NameConstant', lineno=17, col_offset=70, op_type=None, end_lineno=17, end_col_offset=74)
2022-12-14 20:32:35,076: [92mResult: Detected at meeseeks/iam.py: (17, 70)[0m
2022-12-14 20:32:37,578: [91mResult: Survived at meeseeks/iam.py: (17, 70)[0m
2022-12-14 20:32:37,579: [91mBreak on survival: stopping further mutations at location.[0m
2022-12-14 20:32:37,579: Current target location: iam.py, LocIndex(ast_class='NameConstant', lineno=33, col_offset=44, op_type=None, end_lineno=33, end_col_offset=48)
2022-12-14 20:32:40,019: [91mResult: Survived at meeseeks/iam.py: (33, 44)[0m
2022-12-14 20:32:40,021: [91mBreak on survival: stopping further mutations at location.[0m
2022-12-14 20:32:40,022: Current target location: iam.py, LocIndex(ast_class='NameConstant', lineno=33, col_offset=61, op_type=None, end_lineno=33, end_col_offset=65)
2022-12-14 20:32:42,462: [92mResult: Detected at meeseeks/iam.py: (33, 61)[0m
2022-12-14 20:32:44,903: [91mResult: Survived at meeseeks/iam.py: (33, 61)[0m
2022-12-14 20:32:44,904: [91mBreak on survival: stopping further mutations at location.[0m
2022-12-14 20:32:44,904: Current target location: iam.py, LocIndex(ast_class='If', lineno=54, col_offset=8, op_type='If_Statement', end_lineno=55, end_col_offset=32)
2022-12-14 20:32:46,602: [92mResult: Detected at meeseeks/iam.py: (54, 8)[0m
2022-12-14 20:32:49,154: [92mResult: Detected at meeseeks/iam.py: (54, 8)[0m
2022-12-14 20:32:49,154: Current target location: iam.py, LocIndex(ast_class='CompareIs', lineno=54, col_offset=11, op_type=<class '_ast.Is'>, end_lineno=54, end_col_offset=31)
2022-12-14 20:32:51,109: [92mResult: Detected at meeseeks/iam.py: (54, 11)[0m
2022-12-14 20:32:51,110: Current target location: iam.py, LocIndex(ast_class='NameConstant', lineno=54, col_offset=27, op_type=None, end_lineno=54, end_col_offset=31)
2022-12-14 20:32:53,048: [92mResult: Detected at meeseeks/iam.py: (54, 27)[0m
2022-12-14 20:32:55,175: [92mResult: Detected at meeseeks/iam.py: (54, 27)[0m
2022-12-14 20:32:55,175: Current target location: iam.py, LocIndex(ast_class='NameConstant', lineno=55, col_offset=27, op_type=False, end_lineno=55, end_col_offset=32)
2022-12-14 20:32:57,963: [92mResult: Detected at meeseeks/iam.py: (55, 27)[0m
2022-12-14 20:32:59,909: [92mResult: Detected at meeseeks/iam.py: (55, 27)[0m
2022-12-14 20:32:59,910: Current target location: iam.py, LocIndex(ast_class='If', lineno=56, col_offset=8, op_type='If_Statement', end_lineno=57, end_col_offset=19)
2022-12-14 20:33:02,527: [92mResult: Detected at meeseeks/iam.py: (56, 8)[0m
2022-12-14 20:33:05,208: [92mResult: Detected at meeseeks/iam.py: (56, 8)[0m
2022-12-14 20:33:05,208: Current target location: iam.py, LocIndex(ast_class='CompareIs', lineno=56, col_offset=11, op_type=<class '_ast.Is'>, end_lineno=56, end_col_offset=22)
2022-12-14 20:33:07,953: [92mResult: Detected at meeseeks/iam.py: (56, 11)[0m
2022-12-14 20:33:07,953: Current target location: iam.py, LocIndex(ast_class='NameConstant', lineno=56, col_offset=18, op_type=None, end_lineno=56, end_col_offset=22)
2022-12-14 20:33:10,602: [92mResult: Detected at meeseeks/iam.py: (56, 18)[0m
2022-12-14 20:33:13,272: [92mResult: Detected at meeseeks/iam.py: (56, 18)[0m
2022-12-14 20:33:13,272: Current target location: iam.py, LocIndex(ast_class='If', lineno=59, col_offset=8, op_type='If_Statement', end_lineno=63, end_col_offset=13)
2022-12-14 20:33:15,714: [92mResult: Detected at meeseeks/iam.py: (59, 8)[0m
2022-12-14 20:33:16,399: [92mResult: Detected at meeseeks/iam.py: (59, 8)[0m
2022-12-14 20:33:16,399: Current target location: iam.py, LocIndex(ast_class='BoolOp', lineno=59, col_offset=11, op_type=<class '_ast.Or'>, end_lineno=59, end_col_offset=73)
2022-12-14 20:33:18,893: [92mResult: Detected at meeseeks/iam.py: (59, 11)[0m
2022-12-14 20:33:18,894: Current target location: iam.py, LocIndex(ast_class='If', lineno=101, col_offset=8, op_type='If_Statement', end_lineno=113, end_col_offset=31)
2022-12-14 20:33:19,507: [92mResult: Detected at meeseeks/iam.py: (101, 8)[0m
2022-12-14 20:33:20,188: [92mResult: Detected at meeseeks/iam.py: (101, 8)[0m
2022-12-14 20:33:20,188: Current target location: iam.py, LocIndex(ast_class='If', lineno=104, col_offset=12, op_type='If_Statement', end_lineno=113, end_col_offset=31)
2022-12-14 20:33:22,715: [92mResult: Detected at meeseeks/iam.py: (104, 12)[0m
2022-12-14 20:33:23,296: [92mResult: Detected at meeseeks/iam.py: (104, 12)[0m
2022-12-14 20:33:23,296: Current target location: iam.py, LocIndex(ast_class='If', lineno=130, col_offset=12, op_type='If_Statement', end_lineno=149, end_col_offset=17)
2022-12-14 20:33:25,811: [92mResult: Detected at meeseeks/iam.py: (130, 12)[0m
2022-12-14 20:33:28,284: [92mResult: Detected at meeseeks/iam.py: (130, 12)[0m
2022-12-14 20:33:28,284: Current target location: iam.py, LocIndex(ast_class='If', lineno=131, col_offset=16, op_type='If_Statement', end_lineno=134, end_col_offset=42)
2022-12-14 20:33:30,782: [92mResult: Detected at meeseeks/iam.py: (131, 16)[0m
2022-12-14 20:33:32,304: [92mResult: Detected at meeseeks/iam.py: (131, 16)[0m
2022-12-14 20:33:32,304: Current target location: iam.py, LocIndex(ast_class='If', lineno=142, col_offset=16, op_type='If_Statement', end_lineno=145, end_col_offset=42)
2022-12-14 20:33:34,799: [92mResult: Detected at meeseeks/iam.py: (142, 16)[0m
2022-12-14 20:33:36,336: [92mResult: Detected at meeseeks/iam.py: (142, 16)[0m
2022-12-14 20:33:36,336: Current target location: iam.py, LocIndex(ast_class='If', lineno=180, col_offset=8, op_type='If_Statement', end_lineno=181, end_col_offset=64)
2022-12-14 20:33:38,826: [92mResult: Detected at meeseeks/iam.py: (180, 8)[0m
2022-12-14 20:33:40,423: [92mResult: Detected at meeseeks/iam.py: (180, 8)[0m
2022-12-14 20:33:40,423: Current target location: iam.py, LocIndex(ast_class='CompareIs', lineno=180, col_offset=11, op_type=<class '_ast.Is'>, end_lineno=180, end_col_offset=58)
2022-12-14 20:33:42,017: [92mResult: Detected at meeseeks/iam.py: (180, 11)[0m
2022-12-14 20:33:42,017: Current target location: iam.py, LocIndex(ast_class='NameConstant', lineno=180, col_offset=54, op_type=None, end_lineno=180, end_col_offset=58)
2022-12-14 20:33:43,623: [92mResult: Detected at meeseeks/iam.py: (180, 54)[0m
2022-12-14 20:33:45,201: [92mResult: Detected at meeseeks/iam.py: (180, 54)[0m
2022-12-14 20:33:45,202: Current target location: iam.py, LocIndex(ast_class='If', lineno=214, col_offset=8, op_type='If_Statement', end_lineno=222, end_col_offset=52)
2022-12-14 20:33:46,834: [92mResult: Detected at meeseeks/iam.py: (214, 8)[0m
2022-12-14 20:33:49,326: [92mResult: Detected at meeseeks/iam.py: (214, 8)[0m
2022-12-14 20:33:49,326: Current target location: iam.py, LocIndex(ast_class='If', lineno=215, col_offset=12, op_type='If_Statement', end_lineno=222, end_col_offset=52)
2022-12-14 20:33:50,871: [92mResult: Detected at meeseeks/iam.py: (215, 12)[0m
2022-12-14 20:33:53,368: [92mResult: Detected at meeseeks/iam.py: (215, 12)[0m
2022-12-14 20:33:53,368: Current target location: iam.py, LocIndex(ast_class='If', lineno=216, col_offset=16, op_type='If_Statement', end_lineno=222, end_col_offset=52)
2022-12-14 20:33:55,825: [92mResult: Detected at meeseeks/iam.py: (216, 16)[0m
2022-12-14 20:33:58,286: [92mResult: Detected at meeseeks/iam.py: (216, 16)[0m
2022-12-14 20:33:58,286: Current target location: iam.py, LocIndex(ast_class='BinOp', lineno=217, col_offset=34, op_type=<class '_ast.Add'>, end_lineno=217, end_col_offset=74)
2022-12-14 20:34:00,751: [92mResult: Detected at meeseeks/iam.py: (217, 34)[0m
2022-12-14 20:34:03,224: [92mResult: Detected at meeseeks/iam.py: (217, 34)[0m
2022-12-14 20:34:05,694: [92mResult: Detected at meeseeks/iam.py: (217, 34)[0m
2022-12-14 20:34:08,140: [92mResult: Detected at meeseeks/iam.py: (217, 34)[0m
2022-12-14 20:34:10,585: [92mResult: Detected at meeseeks/iam.py: (217, 34)[0m
2022-12-14 20:34:13,076: [92mResult: Detected at meeseeks/iam.py: (217, 34)[0m
2022-12-14 20:34:13,076: Current target location: iam.py, LocIndex(ast_class='If', lineno=218, col_offset=20, op_type='If_Statement', end_lineno=219, end_col_offset=56)
2022-12-14 20:34:15,536: [92mResult: Detected at meeseeks/iam.py: (218, 20)[0m
2022-12-14 20:34:17,993: [92mResult: Detected at meeseeks/iam.py: (218, 20)[0m
2022-12-14 20:34:17,993: Current target location: iam.py, LocIndex(ast_class='Compare', lineno=218, col_offset=23, op_type=<class '_ast.GtE'>, end_lineno=218, end_col_offset=67)
2022-12-14 20:34:20,449: [92mResult: Detected at meeseeks/iam.py: (218, 23)[0m
2022-12-14 20:34:22,918: [92mResult: Detected at meeseeks/iam.py: (218, 23)[0m
2022-12-14 20:34:25,399: [92mResult: Detected at meeseeks/iam.py: (218, 23)[0m
2022-12-14 20:34:28,033: [92mResult: Detected at meeseeks/iam.py: (218, 23)[0m
2022-12-14 20:34:30,670: [92mResult: Detected at meeseeks/iam.py: (218, 23)[0m
2022-12-14 20:34:30,670: Current target location: iam.py, LocIndex(ast_class='If', lineno=269, col_offset=8, op_type='If_Statement', end_lineno=276, end_col_offset=48)
2022-12-14 20:34:33,199: [92mResult: Detected at meeseeks/iam.py: (269, 8)[0m
2022-12-14 20:34:34,874: [92mResult: Detected at meeseeks/iam.py: (269, 8)[0m
2022-12-14 20:34:34,874: Current target location: iam.py, LocIndex(ast_class='If', lineno=270, col_offset=12, op_type='If_Statement', end_lineno=276, end_col_offset=48)
2022-12-14 20:34:37,461: [92mResult: Detected at meeseeks/iam.py: (270, 12)[0m
2022-12-14 20:34:39,957: [92mResult: Detected at meeseeks/iam.py: (270, 12)[0m
2022-12-14 20:34:39,957: Current target location: iam.py, LocIndex(ast_class='BinOp', lineno=271, col_offset=30, op_type=<class '_ast.Add'>, end_lineno=271, end_col_offset=70)
2022-12-14 20:34:42,551: [92mResult: Detected at meeseeks/iam.py: (271, 30)[0m
2022-12-14 20:34:45,372: [92mResult: Detected at meeseeks/iam.py: (271, 30)[0m
2022-12-14 20:34:47,995: [92mResult: Detected at meeseeks/iam.py: (271, 30)[0m
2022-12-14 20:34:50,470: [92mResult: Detected at meeseeks/iam.py: (271, 30)[0m
2022-12-14 20:34:52,949: [92mResult: Detected at meeseeks/iam.py: (271, 30)[0m
2022-12-14 20:34:55,408: [92mResult: Detected at meeseeks/iam.py: (271, 30)[0m
2022-12-14 20:34:55,408: Current target location: iam.py, LocIndex(ast_class='If', lineno=272, col_offset=16, op_type='If_Statement', end_lineno=273, end_col_offset=52)
2022-12-14 20:34:57,877: [92mResult: Detected at meeseeks/iam.py: (272, 16)[0m
2022-12-14 20:35:00,347: [92mResult: Detected at meeseeks/iam.py: (272, 16)[0m
2022-12-14 20:35:00,347: Current target location: iam.py, LocIndex(ast_class='Compare', lineno=272, col_offset=19, op_type=<class '_ast.GtE'>, end_lineno=272, end_col_offset=63)
2022-12-14 20:35:02,950: [92mResult: Detected at meeseeks/iam.py: (272, 19)[0m
2022-12-14 20:35:05,449: [92mResult: Detected at meeseeks/iam.py: (272, 19)[0m
2022-12-14 20:35:07,938: [92mResult: Detected at meeseeks/iam.py: (272, 19)[0m
2022-12-14 20:35:10,488: [92mResult: Detected at meeseeks/iam.py: (272, 19)[0m
2022-12-14 20:35:13,143: [92mResult: Detected at meeseeks/iam.py: (272, 19)[0m
2022-12-14 20:35:13,144: Running clean trial
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
meeseeks/iam.py                               119      0   100%
meeseeks/src/__init__.py                        0      0   100%
meeseeks/src/hash/__init__.py                   0      0   100%
meeseeks/src/hash/args_and_kwargs_hash.py       7      0   100%
-------------------------------------------------------------------------
TOTAL                                         127      0   100%


============================== 40 passed in 2.19s ==============================
2022-12-14 20:35:15,581: CLI Report:

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
 - Clean trial 1 run time: 0:00:02.660132
 - Clean trial 2 run time: 0:00:02.436114
 - Mutation trials total run time: 0:02:48.845720

2022-12-14 20:35:15,581: Trial Summary Report:

Overall mutation trial summary
==============================
 - SURVIVED: 5
 - DETECTED: 69
 - TOTAL RUNS: 74
 - RUN DATETIME: 2022-12-14 20:35:15.581150

2022-12-14 20:35:15,581: Detected mutations:[92m

DETECTED
--------
 - meeseeks/iam.py: (l: 17, c: 53) - mutation from None to True
 - meeseeks/iam.py: (l: 17, c: 70) - mutation from None to True
 - meeseeks/iam.py: (l: 33, c: 61) - mutation from None to True
 - meeseeks/iam.py: (l: 54, c: 8) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 54, c: 8) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 54, c: 11) - mutation from <class '_ast.Is'> to <class '_ast.IsNot'>
 - meeseeks/iam.py: (l: 54, c: 27) - mutation from None to False
 - meeseeks/iam.py: (l: 54, c: 27) - mutation from None to True
 - meeseeks/iam.py: (l: 55, c: 27) - mutation from False to True
 - meeseeks/iam.py: (l: 55, c: 27) - mutation from False to None
 - meeseeks/iam.py: (l: 56, c: 8) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 56, c: 8) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 56, c: 11) - mutation from <class '_ast.Is'> to <class '_ast.IsNot'>
 - meeseeks/iam.py: (l: 56, c: 18) - mutation from None to False
 - meeseeks/iam.py: (l: 56, c: 18) - mutation from None to True
 - meeseeks/iam.py: (l: 59, c: 8) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 59, c: 8) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 59, c: 11) - mutation from <class '_ast.Or'> to <class '_ast.And'>
 - meeseeks/iam.py: (l: 101, c: 8) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 101, c: 8) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 104, c: 12) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 104, c: 12) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 130, c: 12) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 130, c: 12) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 131, c: 16) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 131, c: 16) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 142, c: 16) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 142, c: 16) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 180, c: 8) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 180, c: 8) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 180, c: 11) - mutation from <class '_ast.Is'> to <class '_ast.IsNot'>
 - meeseeks/iam.py: (l: 180, c: 54) - mutation from None to True
 - meeseeks/iam.py: (l: 180, c: 54) - mutation from None to False
 - meeseeks/iam.py: (l: 214, c: 8) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 214, c: 8) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 215, c: 12) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 215, c: 12) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 216, c: 16) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 216, c: 16) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 217, c: 34) - mutation from <class '_ast.Add'> to <class '_ast.Pow'>
 - meeseeks/iam.py: (l: 217, c: 34) - mutation from <class '_ast.Add'> to <class '_ast.Mult'>
 - meeseeks/iam.py: (l: 217, c: 34) - mutation from <class '_ast.Add'> to <class '_ast.Sub'>
 - meeseeks/iam.py: (l: 217, c: 34) - mutation from <class '_ast.Add'> to <class '_ast.FloorDiv'>
 - meeseeks/iam.py: (l: 217, c: 34) - mutation from <class '_ast.Add'> to <class '_ast.Div'>
 - meeseeks/iam.py: (l: 217, c: 34) - mutation from <class '_ast.Add'> to <class '_ast.Mod'>
 - meeseeks/iam.py: (l: 218, c: 20) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 218, c: 20) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 218, c: 23) - mutation from <class '_ast.GtE'> to <class '_ast.LtE'>
 - meeseeks/iam.py: (l: 218, c: 23) - mutation from <class '_ast.GtE'> to <class '_ast.Gt'>
 - meeseeks/iam.py: (l: 218, c: 23) - mutation from <class '_ast.GtE'> to <class '_ast.Lt'>
 - meeseeks/iam.py: (l: 218, c: 23) - mutation from <class '_ast.GtE'> to <class '_ast.Eq'>
 - meeseeks/iam.py: (l: 218, c: 23) - mutation from <class '_ast.GtE'> to <class '_ast.NotEq'>
 - meeseeks/iam.py: (l: 269, c: 8) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 269, c: 8) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 270, c: 12) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 270, c: 12) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 271, c: 30) - mutation from <class '_ast.Add'> to <class '_ast.Sub'>
 - meeseeks/iam.py: (l: 271, c: 30) - mutation from <class '_ast.Add'> to <class '_ast.Mult'>
 - meeseeks/iam.py: (l: 271, c: 30) - mutation from <class '_ast.Add'> to <class '_ast.Mod'>
 - meeseeks/iam.py: (l: 271, c: 30) - mutation from <class '_ast.Add'> to <class '_ast.Div'>
 - meeseeks/iam.py: (l: 271, c: 30) - mutation from <class '_ast.Add'> to <class '_ast.FloorDiv'>
 - meeseeks/iam.py: (l: 271, c: 30) - mutation from <class '_ast.Add'> to <class '_ast.Pow'>
 - meeseeks/iam.py: (l: 272, c: 16) - mutation from If_Statement to If_True
 - meeseeks/iam.py: (l: 272, c: 16) - mutation from If_Statement to If_False
 - meeseeks/iam.py: (l: 272, c: 19) - mutation from <class '_ast.GtE'> to <class '_ast.Eq'>
 - meeseeks/iam.py: (l: 272, c: 19) - mutation from <class '_ast.GtE'> to <class '_ast.LtE'>
 - meeseeks/iam.py: (l: 272, c: 19) - mutation from <class '_ast.GtE'> to <class '_ast.Lt'>
 - meeseeks/iam.py: (l: 272, c: 19) - mutation from <class '_ast.GtE'> to <class '_ast.Gt'>
 - meeseeks/iam.py: (l: 272, c: 19) - mutation from <class '_ast.GtE'> to <class '_ast.NotEq'>[0m

2022-12-14 20:35:15,581: Timedout mutations:

2022-12-14 20:35:15,581: Surviving mutations:[91m

SURVIVED
--------
 - meeseeks/iam.py: (l: 10, c: 35) - mutation from False to None
 - meeseeks/iam.py: (l: 17, c: 53) - mutation from None to False
 - meeseeks/iam.py: (l: 17, c: 70) - mutation from None to False
 - meeseeks/iam.py: (l: 33, c: 44) - mutation from None to False
 - meeseeks/iam.py: (l: 33, c: 61) - mutation from None to False[0m

```

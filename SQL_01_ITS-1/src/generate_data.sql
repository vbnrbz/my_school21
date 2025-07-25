INSERT INTO patients (patient_id, "name", age, gender, "condition") VALUES
    (1, 'Панова Серафима Дамировна', 30, 'Female', 'Камни в желчном пузыре'),
    (2, 'Андреев Андрей Даниилович', 39, 'Male', 'Депрессия'),
    (3, 'Кузнецов Владимир Владиславович', 40, 'Male', 'Гепатит'),
    (4, 'Гришин Артём Дмитриевич', 34, 'Male', 'Сахарный диабет'),
    (5, 'Евсеев Александр Михайлович', 50, 'Male', 'Псориаз'),
    (6, 'Савина Василиса Романовна', 51, 'Female', 'Псориаз'),
    (7, 'Демин Иван Глебович', 59, 'Male', 'Гепатит'),
    (8, 'Егоров Дмитрий Ярославович', 49, 'Male', 'Депрессия'),
    (9, 'Гуляев Савелий Романович', 10, 'Male', 'Депрессия'),
    (10, 'Сальников Константин Игоревич', 33, 'Male', 'Гепатит'),
    (11, 'Гусев Илья Русланович', 44, 'Male', 'Грипп'),
    (12, 'Соколов Сергей Алексеевич', 31, 'Male', 'Цистит'),
    (13, 'Федорова Аврора Андреевна', 49, 'Female', 'Грипп'),
    (14, 'Зотова Анастасия Максимовна', 30, 'Female', 'Гастрит'),
    (15, 'Воробьев Дамир Александрович', 31, 'Male', 'Грипп'),
    (16, 'Егорова Алиса Михайловна', 32, 'Female', 'Цистит'),
    (17, 'Исакова Варвара Владимировна', 23, 'Female', 'Грипп'),
    (18, 'Селиванов Артём Михайлович', 54, 'Male', 'Цистит'),
    (19, 'Васильева Ксения Романовна', 34, 'Female', 'Цистит'),
    (20, 'Блохина Фатима Степановна', 23, 'Female', 'Гастрит'),
    (21, 'Кузина Мария Александровна', 43, 'Female', 'Гастрит');

INSERT INTO trials (trial_id, trial_name, "start_date", end_date) VALUES 
    (1, 'Исследование на тонкость полотенца', '2024-01-01', '2024-01-02'),
    (2, 'Исследование на слои туалетной бумаги', '2024-02-01', '2024-02-02'),
    (3, 'Исследование на яркость лампочки', '2024-03-01', '2024-03-02'),
    (4, 'Исследование на запах курицы', '2024-04-01', '2024-04-02'),
    (5, 'Коллективное исследование на победителя в нарды', '2024-05-01', '2024-05-02'),
    (6, 'Исследование на исследование', '2024-06-01', '2024-06-02');

INSERT INTO measurements (measurement_id, patient_id, trial_id, measurement_date, drug, condition_score) VALUES
    (1, 11, 6, '2024-10-10', 'Клавиатура', 88),
    (2, 6, 1, '2024-10-10', 'Плацебо', 4),
    (3, 11, 5, '2024-10-10', 'Плацебо', 69),
    (4, 11, 2, '2024-10-10', 'Плацебо', 96),
    (5, 6, 2, '2024-10-10', 'Плацебо', 84),
    (6, 1, 4, '2024-10-10', 'Плацебо', 84),
    (7, 12, 1, '2024-10-10', 'Клавиатура', 83),
    (8, 1, 1, '2024-10-10', 'Клавиатура', 52),
    (9, 15, 3, '2024-10-10', 'Плацебо', 51),
    (10, 6, 5, '2024-10-10', 'Клавиатура', 14),
    (11, 16, 3, '2024-10-10', 'Клавиатура', 22),
    (12, 6, 1, '2024-10-10', 'Плацебо', 35),
    (13, 8, 1, '2024-10-10', 'Плацебо', 62),
    (14, 9, 3, '2024-10-10', 'Плацебо', 47),
    (15, 14, 4, '2024-10-10', 'Плацебо', 80),
    (16, 8, 5, '2024-10-10', 'Клавиатура', 24),
    (17, 19, 4, '2024-10-10', 'Плацебо', 31),
    (18, 4, 3, '2024-10-10', 'Плацебо', 82),
    (19, 14, 5, '2024-10-10', 'Клавиатура', 3),
    (20, 2, 6, '2024-10-10', 'Плацебо', 31),
    (21, 21, 4, '2024-10-10', 'Клавиатура', 62),
    (22, 21, 6, '2024-10-10', 'Плацебо', 92),
    (23, 20, 6, '2024-10-10', 'Клавиатура', 97),
    (24, 19, 6, '2024-10-10', 'Плацебо', 31),
    (25, 7, 4, '2024-10-10', 'Клавиатура', 82),
    (26, 20, 3, '2024-10-10', 'Клавиатура', 84),
    (27, 16, 5, '2024-10-10', 'Клавиатура', 48),
    (28, 14, 6, '2024-10-10', 'Плацебо', 32),
    (29, 21, 2, '2024-10-10', 'Плацебо', 31),
    (30, 12, 4, '2024-10-10', 'Клавиатура', 28),
    (31, 4, 2, '2024-10-10', 'Клавиатура', 18),
    (32, 7, 1, '2024-10-10', 'Клавиатура', 80),
    (33, 20, 6, '2024-10-10', 'Плацебо', 62),
    (34, 19, 2, '2024-10-10', 'Плацебо', 50),
    (35, 3, 3, '2024-10-10', 'Клавиатура', 80),
    (36, 18, 6, '2024-10-10', 'Клавиатура', 33),
    (37, 9, 4, '2024-10-10', 'Клавиатура', 6),
    (38, 1, 5, '2024-10-10', 'Плацебо', 94),
    (39, 10, 3, '2024-10-10', 'Плацебо', 22),
    (40, 21, 5, '2024-10-10', 'Плацебо', 65),
    (41, 2, 4, '2024-10-10', 'Клавиатура', 98),
    (42, 15, 2, '2024-10-10', 'Плацебо', 28),
    (43, 19, 2, '2024-10-10', 'Клавиатура', 27),
    (44, 6, 3, '2024-10-10', 'Клавиатура', 86),
    (45, 21, 2, '2024-10-10', 'Плацебо', 40),
    (46, 8, 2, '2024-10-10', 'Клавиатура', 36),
    (47, 2, 3, '2024-10-10', 'Клавиатура', 18),
    (48, 18, 5, '2024-10-10', 'Плацебо', 14),
    (49, 17, 5, '2024-10-10', 'Клавиатура', 86),
    (50, 4, 2, '2024-10-10', 'Плацебо', 31),
    (51, 4, 6, '2024-10-10', 'Плацебо', 69),
    (52, 4, 4, '2024-10-10', 'Плацебо', 56),
    (53, 4, 2, '2024-10-10', 'Плацебо', 78),
    (54, 13, 4, '2024-10-10', 'Клавиатура', 33),
    (55, 3, 2, '2024-10-10', 'Клавиатура', 11),
    (56, 20, 6, '2024-10-10', 'Плацебо', 85),
    (57, 1, 1, '2024-10-10', 'Плацебо', 50),
    (58, 20, 2, '2024-10-10', 'Клавиатура', 16),
    (59, 18, 3, '2024-10-10', 'Плацебо', 53),
    (60, 8, 1, '2024-10-10', 'Плацебо', 51),
    (61, 10, 3, '2024-10-10', 'Плацебо', 63),
    (62, 11, 5, '2024-10-10', 'Плацебо', 25),
    (63, 3, 6, '2024-10-10', 'Клавиатура', 64),
    (64, 20, 5, '2024-10-10', 'Плацебо', 70),
    (65, 5, 2, '2024-10-10', 'Плацебо', 64),
    (66, 19, 6, '2024-10-10', 'Плацебо', 85),
    (67, 14, 2, '2024-10-10', 'Клавиатура', 49),
    (68, 11, 6, '2024-10-10', 'Плацебо', 91),
    (69, 20, 5, '2024-10-10', 'Клавиатура', 35),
    (70, 21, 3, '2024-10-10', 'Клавиатура', 48),
    (71, 15, 6, '2024-10-10', 'Клавиатура', 67),
    (72, 4, 4, '2024-10-10', 'Плацебо', 84),
    (73, 11, 5, '2024-10-10', 'Плацебо', 19),
    (74, 3, 1, '2024-10-10', 'Плацебо', 82),
    (75, 13, 6, '2024-10-10', 'Клавиатура', 39),
    (76, 8, 1, '2024-10-10', 'Плацебо', 43),
    (77, 11, 2, '2024-10-10', 'Плацебо', 60),
    (78, 8, 6, '2024-10-10', 'Плацебо', 91),
    (79, 1, 6, '2024-10-10', 'Клавиатура', 69),
    (80, 21, 4, '2024-10-10', 'Клавиатура', 100),
    (81, 21, 2, '2024-10-10', 'Плацебо', 37),
    (82, 1, 5, '2024-10-10', 'Клавиатура', 76),
    (83, 18, 2, '2024-10-10', 'Плацебо', 16),
    (84, 12, 5, '2024-10-10', 'Клавиатура', 35),
    (85, 9, 6, '2024-10-10', 'Клавиатура', 62),
    (86, 3, 4, '2024-10-10', 'Плацебо', 50),
    (87, 21, 6, '2024-10-10', 'Плацебо', 97),
    (88, 18, 5, '2024-10-10', 'Плацебо', 20),
    (89, 9, 2, '2024-10-10', 'Плацебо', 85),
    (90, 17, 4, '2024-10-10', 'Клавиатура', 84),
    (91, 20, 3, '2024-10-10', 'Плацебо', 95),
    (92, 21, 5, '2024-10-10', 'Клавиатура', 91),
    (93, 3, 3, '2024-10-10', 'Клавиатура', 14),
    (94, 15, 3, '2024-10-10', 'Плацебо', 58),
    (95, 4, 2, '2024-10-10', 'Плацебо', 85),
    (96, 16, 1, '2024-10-10', 'Клавиатура', 5),
    (97, 4, 2, '2024-10-10', 'Плацебо', 49),
    (98, 12, 4, '2024-10-10', 'Клавиатура', 53),
    (99, 19, 1, '2024-10-10', 'Плацебо', 41),
    (100, 11, 1, '2024-10-10', 'Клавиатура', 14),
    (101, 8, 5, '2024-10-10', 'Клавиатура', 37),
    (102, 20, 1, '2024-10-10', 'Плацебо', 63),
    (103, 2, 2, '2024-10-10', 'Плацебо', 85),
    (104, 17, 1, '2024-10-10', 'Плацебо', 51),
    (105, 8, 4, '2024-10-10', 'Плацебо', 42),
    (106, 1, 1, '2024-10-10', 'Плацебо', 50),
    (107, 14, 4, '2024-10-10', 'Клавиатура', 35),
    (108, 7, 3, '2024-10-10', 'Клавиатура', 54),
    (109, 17, 3, '2024-10-10', 'Плацебо', 0),
    (110, 2, 1, '2024-10-10', 'Клавиатура', 75),
    (111, 17, 1, '2024-10-10', 'Клавиатура', 0),
    (112, 3, 1, '2024-10-10', 'Плацебо', 56),
    (113, 1, 2, '2024-10-10', 'Плацебо', 70),
    (114, 7, 5, '2024-10-10', 'Клавиатура', 30),
    (115, 13, 1, '2024-10-10', 'Плацебо', 61),
    (116, 1, 1, '2024-10-10', 'Плацебо', 86),
    (117, 1, 4, '2024-10-10', 'Плацебо', 35),
    (118, 15, 3, '2024-10-10', 'Плацебо', 4),
    (119, 16, 1, '2024-10-10', 'Плацебо', 37),
    (120, 6, 3, '2024-10-10', 'Плацебо', 5),
    (121, 6, 4, '2024-10-10', 'Плацебо', 62),
    (122, 13, 3, '2024-10-10', 'Клавиатура', 19),
    (123, 10, 3, '2024-10-10', 'Плацебо', 87),
    (124, 8, 6, '2024-10-10', 'Плацебо', 12),
    (125, 10, 2, '2024-10-10', 'Клавиатура', 22),
    (126, 11, 3, '2024-10-10', 'Клавиатура', 57),
    (127, 12, 6, '2024-10-10', 'Плацебо', 42),
    (128, 21, 6, '2024-10-10', 'Плацебо', 90),
    (129, 1, 5, '2024-10-10', 'Плацебо', 46),
    (130, 14, 5, '2024-10-10', 'Плацебо', 36),
    (131, 15, 4, '2024-10-10', 'Клавиатура', 94),
    (132, 2, 2, '2024-10-10', 'Плацебо', 58),
    (133, 13, 1, '2024-10-10', 'Клавиатура', 53),
    (134, 4, 1, '2024-10-10', 'Клавиатура', 74),
    (135, 21, 4, '2024-10-10', 'Клавиатура', 69),
    (136, 6, 4, '2024-10-10', 'Плацебо', 42),
    (137, 19, 4, '2024-10-10', 'Плацебо', 98),
    (138, 1, 4, '2024-10-10', 'Клавиатура', 88),
    (139, 6, 4, '2024-10-10', 'Клавиатура', 55),
    (140, 10, 4, '2024-10-10', 'Плацебо', 54),
    (141, 20, 5, '2024-10-10', 'Клавиатура', 26),
    (142, 7, 2, '2024-10-10', 'Клавиатура', 15),
    (143, 19, 2, '2024-10-10', 'Клавиатура', 89),
    (144, 7, 2, '2024-10-10', 'Плацебо', 35),
    (145, 18, 1, '2024-10-10', 'Плацебо', 28),
    (146, 13, 6, '2024-10-10', 'Плацебо', 9),
    (147, 11, 3, '2024-10-10', 'Плацебо', 9),
    (148, 18, 1, '2024-10-10', 'Плацебо', 2),
    (149, 8, 1, '2024-10-10', 'Клавиатура', 71),
    (150, 5, 3, '2024-10-10', 'Клавиатура', 1),
    (151, 2, 3, '2024-10-10', 'Плацебо', 9),
    (152, 11, 4, '2024-10-10', 'Клавиатура', 24),
    (153, 14, 1, '2024-10-10', 'Плацебо', 1),
    (154, 21, 3, '2024-10-10', 'Плацебо', 58),
    (155, 21, 2, '2024-10-10', 'Клавиатура', 72),
    (156, 8, 4, '2024-10-10', 'Плацебо', 21),
    (157, 9, 4, '2024-10-10', 'Плацебо', 46),
    (158, 5, 5, '2024-10-10', 'Плацебо', 98),
    (159, 20, 5, '2024-10-10', 'Клавиатура', 60),
    (160, 14, 5, '2024-10-10', 'Клавиатура', 56),
    (161, 18, 5, '2024-10-10', 'Плацебо', 2),
    (162, 10, 2, '2024-10-10', 'Клавиатура', 37),
    (163, 14, 5, '2024-10-10', 'Плацебо', 91),
    (164, 17, 4, '2024-10-10', 'Плацебо', 30),
    (165, 11, 1, '2024-10-10', 'Клавиатура', 84),
    (166, 7, 5, '2024-10-10', 'Клавиатура', 62),
    (167, 20, 6, '2024-10-10', 'Плацебо', 64),
    (168, 17, 1, '2024-10-10', 'Клавиатура', 77),
    (169, 10, 6, '2024-10-10', 'Плацебо', 93),
    (170, 12, 4, '2024-10-10', 'Клавиатура', 84),
    (171, 2, 6, '2024-10-10', 'Клавиатура', 26),
    (172, 3, 4, '2024-10-10', 'Плацебо', 46),
    (173, 4, 3, '2024-10-10', 'Клавиатура', 71),
    (174, 10, 2, '2024-10-10', 'Плацебо', 69),
    (175, 5, 3, '2024-10-10', 'Плацебо', 60),
    (176, 9, 1, '2024-10-10', 'Клавиатура', 69),
    (177, 5, 4, '2024-10-10', 'Клавиатура', 7),
    (178, 20, 2, '2024-10-10', 'Плацебо', 80),
    (179, 1, 4, '2024-10-10', 'Плацебо', 74),
    (180, 12, 4, '2024-10-10', 'Плацебо', 90),
    (181, 13, 4, '2024-10-10', 'Клавиатура', 82),
    (182, 7, 4, '2024-10-10', 'Плацебо', 20),
    (183, 17, 1, '2024-10-10', 'Плацебо', 32),
    (184, 15, 1, '2024-10-10', 'Плацебо', 83),
    (185, 21, 4, '2024-10-10', 'Клавиатура', 89),
    (186, 10, 2, '2024-10-10', 'Плацебо', 57),
    (187, 18, 6, '2024-10-10', 'Клавиатура', 51),
    (188, 2, 4, '2024-10-10', 'Плацебо', 94),
    (189, 14, 2, '2024-10-10', 'Клавиатура', 20),
    (190, 10, 2, '2024-10-10', 'Клавиатура', 79),
    (191, 10, 1, '2024-10-10', 'Плацебо', 0),
    (192, 7, 6, '2024-10-10', 'Клавиатура', 42),
    (193, 10, 6, '2024-10-10', 'Клавиатура', 24),
    (194, 13, 6, '2024-10-10', 'Клавиатура', 100),
    (195, 6, 4, '2024-10-10', 'Клавиатура', 69),
    (196, 9, 1, '2024-10-10', 'Плацебо', 55),
    (197, 8, 2, '2024-10-10', 'Плацебо', 74),
    (198, 11, 1, '2024-10-10', 'Клавиатура', 18),
    (199, 15, 3, '2024-10-10', 'Клавиатура', 80),
    (200, 9, 1, '2024-10-10', 'Клавиатура', 59),
    (201, 12, 6, '2024-10-10', 'Плацебо', 43);
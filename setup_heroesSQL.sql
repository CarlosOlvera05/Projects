CREATE TABLE heroes (
    id INTEGER PRIMARY KEY,
    name TEXT,
    alias TEXT,
    city TEXT,
    power_level INTEGER,
    team TEXT
);

INSERT INTO heroes (id, name, alias, city, power_level, team) VALUES
(1, 'Bruce Wayne', 'Batman', 'Gotham', 85, 'Justice League'),
(2, 'Clark Kent', 'Superman', 'Metropolis', 100, 'Justice League'),
(3, 'Diana Prince', 'Wonder Woman', 'Themyscira', 98, 'Justice League'),
(4, 'Barry Allen', 'Flash', 'Central City', 95, 'Justice League'),
(5, 'Arthur Curry', 'Aquaman', 'Atlantis', 88, 'Justice League'),
(6, 'Victor Stone', 'Cyborg', 'Detroit', 90, 'Justice League');


CREATE DATABASE ENERGYDB2;
USE ENERGYDB2;

-- create database ENERGYDB3;
-- use ENERGYDB3;


-- CREATE TABLE country (
-- CID VARCHAR(10) PRIMARY KEY,
-- Country VARCHAR(100) UNIQUE) ;


-- CREATE TABLE emission_3 (
--     country VARCHAR(100),
--     energy_type VARCHAR(50),
--     year INT,
--     emission INT,
--     per_capita_emission DOUBLE,
--     FOREIGN KEY (country) REFERENCES country(Country));
--     
--     
--     CREATE TABLE population (
--     countries VARCHAR(100),
--     year INT,
--     Value DOUBLE,
--     FOREIGN KEY (countries) REFERENCES country(Country)
-- );


-- CREATE TABLE production (
--     country VARCHAR(100),
--     energy VARCHAR(50),
--     year INT,
--     production INT,
--     FOREIGN KEY (country) REFERENCES country(Country)
-- );


-- CREATE TABLE gdp_3 (
--     Country VARCHAR(100),
--     year INT,
--     Value DOUBLE,
--     FOREIGN KEY (Country) REFERENCES country(Country)
-- );

-- CREATE TABLE consumption (
--     country VARCHAR(100),
--     energy VARCHAR(50),
--     year INT,
--     consumption INT,
--     FOREIGN KEY (country) REFERENCES country(Country)
-- );

ALTER TABLE country_3
MODIFY Country VARCHAR(100);

ALTER TABLE country_3
ADD PRIMARY KEY (Country);

DESCRIBE consum_3;
ALTER TABLE consum_3
MODIFY country VARCHAR(100);
ALTER TABLE emission_3
MODIFY country VARCHAR(100);
ALTER TABLE gdp_3
MODIFY country VARCHAR(100);
ALTER TABLE population_3
MODIFY countries VARCHAR(100);
ALTER TABLE production_3
MODIFY country VARCHAR(100);


DESC consum_3;
DESC country_3;
DESC emission_3;
DESC gdp_3;
DESC population_3;
DESC production_3;





alter table consum_3
add constraint fk_country foreign key  (country) references country_3 (Country);

alter table emission_3
add constraint fk_country_emmision foreign key  (country) references country_3 (Country);

alter table gdp_3
add constraint fk_country_gdp foreign key  (country) references country_3 (Country);


alter table population_3
add constraint fk_country_population foreign key  (countries) references country_3 (Country);


alter table production_3
add constraint fk_country_poroduction foreign key  (country) references country_3 (Country);

-- INSIGHTS

-- What is the total emission per country for the most recent year available?

SELECT country,
       year,
       SUM(emission) AS total_emission
FROM emission_3
WHERE year = (SELECT MAX(year) FROM emission_3)
GROUP BY country, year;

-- What are the top 5 countries by GDP in the most recent year?
SELECT country,
       year,
       Value AS gdp
FROM gdp_3
WHERE year = (SELECT MAX(year) FROM gdp_3)
ORDER BY Value DESC
LIMIT 5;

-- Compare energy production and consumption by country and year
SELECT 
    p.country,
    p.year,
    p.energy,
    p.production,
    c.consumption
FROM production_3 p
JOIN consum_3 c
    ON p.country = c.country
   AND p.energy = c.energy
   AND p.year = c.year
ORDER BY p.country, p.year;

-- Which energy types contribute most to emissions across all countries?

SELECT 
    `energy type`,
    SUM(emission) AS total_emission
FROM emission_3
GROUP BY `energy type`
ORDER BY total_emission DESC;

-- Trend Analysis Over Time
SELECT year,
       SUM(consumption) AS total_consumption
FROM consum_3
GROUP BY year
ORDER BY year;

-- How have global emissions changed year over year?

SELECT 
    year,
    SUM(emission) AS total_emission
FROM emission_3
GROUP BY year
ORDER BY year;

-- What is the trend in GDP for each country over the given years?
SELECT 
    country,
    year,
    Value AS gdp
FROM gdp_3
ORDER BY country, year;

-- How has population growth affected total emissions in each country?
-- Has energy consumption increased or decreased over the years for major economies?
SELECT 
    country,
    year,
    SUM(consumption) AS total_consumption
FROM consum_3
GROUP BY country, year
ORDER BY country, year;

-- What is the average yearly change in emissions per capita for each country?
-- Ratio & Per Capita Analysis
-- What is the emission-to-GDP ratio for each country by year?
SELECT 
    e.country,
    e.year,
    e.emission,
    g.Value AS gdp,
    (e.emission / g.Value) AS emission_to_gdp_ratio
FROM emission_3 e
JOIN gdp_3 g
    ON e.country = g.country
   AND e.year = g.year
ORDER BY e.country, e.year;

-- What is the energy consumption per capita for each country over the last decade?
-- How does energy production per capita vary across countries?
-- Which countries have the highest energy consumption relative to GDP?
SELECT 
    c.country,
    c.year,
    SUM(c.consumption) / SUM(g.Value) AS consumption_to_gdp_ratio
FROM consum_3 c
JOIN gdp_3 g
    ON c.country = g.country
   AND c.year = g.year
GROUP BY c.country, c.year
ORDER BY consumption_to_gdp_ratio DESC;

-- What is the correlation between GDP growth and energy production growth?
SELECT 
    g.country,
    g.year,
    g.Value AS gdp,
    p.production
FROM gdp_3 g
JOIN production_3 p
    ON g.country = p.country
   AND g.year = p.year;
   
-- Global Comparisons
-- What are the top 10 countries by population and how do their emissions compare?
-- Which countries have improved (reduced) their per capita emissions the most over the last decade?
-- What is the global share (%) of emissions by country
-- What is the global average GDP, emission, and population by year?


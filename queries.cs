docs.Races
.Select(race => new {
    Name = race.name,
    RaceId = race.raceId,
    Year = race.year,
    Results = (object) null,
    }
})

docs.RaceResults
.Select(result => new {
    Name = result.racename,
    RaceId = result.race,
    Year = (object) null,
    Results = new object[] {
        new {
            ConstructorName = result.constructor.name,
            Points = result.points
        }
    }
})

results
.GroupBy(result => result.RaceId)
.Select(g => new {
    Name = (DynamicEnumerable.FirstOrDefault(g, t => t.Name != null)).Name,
    RaceId = g.Key,
    Year = (DynamicEnumerable.FirstOrDefault(g, t => t.Year != null)).Year,
    Results = g
    .Where(r => r.Results != null)
    .SelectMany(r => r.Results, (r, result) => new {
        ConstructorName = result.ConstructorName,
        Points = result.Points
    })
    .GroupBy(c => c.ConstructorName)
    .Select(c => new {
        ConstructorName = c.Key,
        Points = c.Sum(x => x.Points)
    })
})
.Where(y => y.Year >= 2010 && y.Year < 2018)

docs.RaceConstructorResult
.Select(result => new {
    Races = result.Name,
    ConstructorPoints = result.Results.Select(y => y)
})

results
.GroupBy(result => result.Races)
.Select(g => new {
    Races = g.Key,
    ConstructorPoints = g
    .SelectMany(r => r.ConstructorPoints, (r, result) => new {
        ConstructorName = result.ConstructorName,
        Points = result.Points
    })
    .GroupBy(c => c.ConstructorName)
    .Select(c => new {
        ConstructorName = c.Key,
        Points = c.Sum(x => x.Points)
    })
})

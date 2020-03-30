# Password Hash&Salt

## De opdracht

Dit programma heb ik gemaakt in combinatie met een security exercise. Het was de bedoeling om een password storage te maken met behulp van hashing en salting. We kregen een aantal hulpmiddelen/tips om van gebruik te maken. Het programma is dus wel zelf gemaakt maar een aantal dingen kregen we geadviseerd. Bijvoorbeeld het gebruik maken van de bcrypt package. Die bied de mogelijkheid om wachtwoorden te hashen en te salten in golang. De achterliggende werking van hoe hashing en salting werkt heb ik uitgelegd bij mijn security exerise. Een ander voorbeeld dat ik kreeg om te gebruiken is fmt.Scan en dan met een pointer (&). Dit was voor mij niet nieuw dit heb ik namelijk al gekregen bij de richting Technology die ik heb gevolgd. & dient als een soort van verwijzing naar de variabele die daarna volgt. Een aantal van dit soort regels code zijn dus gegeven/geadviseerd. Ik heb ze vervolgens zelf bestudeerd dus ik weet hoe het werkt, maar ik denk dat ik er zelf nog niet op was gekomen. Deze regels heb ik aangeven met comments in mijn code.


***hashAndSalt*** Funtie

De hash een salt functie heb ik gemaakt om het ingeven wachtwoord door de user in een functie te hashen en salten. Dit doe ik door gebruik te maken van :

bcrypt.GenerateFromPassword(pwd, 4)

Dit is een standaard functie uit de bycrypt package. Je stuurt het wachtwoord en de cost waarde mee. De cost waarde is simpel gezegt de moeilijkheidsgraad van de hash. Dit is minimaal 4 dus daar heb ik hem opgezet. Hoe hoger cost waarde is hoe moeiliijker om de hash te kraken, maar het kost ook meer cpu performence om hem te generen. Om mijn code zo snel mogelijk te laten runnen staat die dus minimaal ingesteld.




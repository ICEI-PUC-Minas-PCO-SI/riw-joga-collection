from queue import Full
from pyfutebol import crawler

resultados = crawler.jogos_de_hoje()

arquivo = open('.resultadosJogos.txt', 'w')
arquivo.write(str(resultados))
arquivo.close()

times = ['Atlético-MG', 'Bahia', 'Botafogo', 'Ceará', 'Corinthians', 'Cruzeiro', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Mirassol', 'Palmeiras', 'Red Bull Bragantino', 'Santos', 'Sport', 'São Paulo', 'Vasco da Gama', 'Vitória', 'Amazonas', 'América Mineiro', 'Athletic', 'Athletico Paranaense', 'Atlético Goianiense', 'Avaí', 'Botafogo-SP', 'CRB', 'Chapecoense', 'Coritiba', 'Criciúma', 'Cuiabá', 'Ferroviária', 'Goiás', 'Novorizontino', 'Operario PR', 'Paysandu', 'Remo', 'Vila Nova', 'Volta Redonda', 'ABC', 'Anápolis', 'Botafogo-PB', 'Brusque', 'CSA', 'Caxias do Sul', 'Confiança', 'Figueirense', 'Floresta', 'Guarani', 'Itabaiana', 'Ituano', 'Londrina', 'Maringá', 'Náutico', 'Ponte Preta', 'Retró', 'São Bernardo', 'Tombense', 'Ypiranga','AC Milan','AS Mônaco', 'Arsenal', 'Aston Villa', 'Atalanta', 'Atlético de Madrid', 'Barcelona', 'Bayer Leverkusen', 'Bayern de Munique', 'Benfica', 'Bolonha', 'Borussia Dortmund', 'Brest', 'Celtic', 'Club Brugge', 'Dinamo Zagreb', 'Feyenoord Rotterdam', 'Girona', 'Internazionale', 'Juventus', 'Lille', 'Liverpool', 'Manchester City', 'PSV Eindhoven', 'Paris Saint-Germain', 'RB Leipzig', 'RB Salzburg', 'Real Madrid', 'Red Star Belgrade', 'SK Sturm Graz', 'Shakhtar Donetsk', 'Slovan Bratislava', 'Sparta Prague', 'Sporting CP', 'VfB Stuttgart', 'Young Boys', 'AS Roma', 'AZ Alkmaar', 'Ajax', 'Anderlecht', 'Athletic Club', 'Besiktas', 'Bodo/Glimt', 'Braga', 'Dynamo Kyiv', 'Eintracht Frankfurt', 'FC Midtjylland', 'FC Porto', 'FC Twente', 'FCSB', 'FK Qarabag', 'Fenerbahçe', 'Ferencvaros', 'Galatasaray', 'Hoffenheim', 'IF Elfsborg', 'Ludogorets Razgrad', 'Lyon', 'Lázio', 'Maccabi Tel-Aviv', 'Malmö FF', 'Manchester United', 'Nice', 'Olympiacos', 'PAOK Salonika', 'Rangers', 'Real Sociedad', 'Tottenham Hotspur']
for time in times:
	resultados = crawler.buscar_jogo_por_time(time)
	arquivo = open(time+'.txt', 'w')
	arquivo.write(str(resultados))
	arquivo.close




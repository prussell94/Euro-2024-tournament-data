from teams.team import Team
from teams.quality_distribution import QualityDistribution
from groups.group import Group

dummy_team = Team("", [], QualityDistribution(1.0, .5), QualityDistribution(1.0, .5))

germanyOffensiveQDist = QualityDistribution(2.9, 1.1)
germanyDefensiveQDist = QualityDistribution(0.8, 1.4)

scotlandOffensiveQDist = QualityDistribution(0.8, 1.7)
scotlandDefensiveQDist = QualityDistribution(1.2, 1.5)

switzerlandOffensiveQDist = QualityDistribution(1.4, 1.6)
switzerlandDefensiveQDist = QualityDistribution(0.7, 1.4)

hungaryOffensiveQDist = QualityDistribution(1.2, 1.6)
hungaryDefensiveQDist = QualityDistribution(1.2, 1.4)

germany = Team("Germany", squad=[], offensive_quality_distributon=germanyOffensiveQDist, defensive_quality_distribution=germanyDefensiveQDist)
scotland = Team("Scotland", squad=[], offensive_quality_distributon=scotlandOffensiveQDist, defensive_quality_distribution=scotlandDefensiveQDist)
switzerland = Team("Switzerland", squad=[], offensive_quality_distributon=switzerlandOffensiveQDist, defensive_quality_distribution=switzerlandDefensiveQDist)
hungary = Team("Hungary", squad=[], offensive_quality_distributon=hungaryOffensiveQDist, defensive_quality_distribution=hungaryDefensiveQDist)

spainOffensiveQDist = QualityDistribution(2.5, 1.4)
spainDefensiveQDist = QualityDistribution(0.9, 1.2)

croatiaOffensiveQDist = QualityDistribution(2.2, 1.2)
croatiaDefensiveQDist = QualityDistribution(0.9, 1.5)

italyOffensiveQDist = QualityDistribution(1.9, 0.7)
italyDefensiveQDist = QualityDistribution(0.4, 1.1)

albaniaOffensiveQDist = QualityDistribution(0.8, 1.1)
albaniaDefensiveQDist = QualityDistribution(2.4, 1.4)

spain = Team("Spain", [], spainOffensiveQDist, spainDefensiveQDist)
croatia = Team("Croatia", [], croatiaOffensiveQDist, croatiaDefensiveQDist)
italy = Team("Italy", [], italyOffensiveQDist, italyDefensiveQDist)
albania = Team("Albania", [], albaniaOffensiveQDist, albaniaDefensiveQDist)

sloveniaOffensiveQDist = QualityDistribution(0.8, 1.4)
sloveniaDefensiveQDist = QualityDistribution(1.5, 1.2)

denmarkOffensiveQDist = QualityDistribution(1.7, 1.1)
denmarkDefensiveQDist = QualityDistribution(1.2, 1.3)

serbiaOffensiveQDist = QualityDistribution(1.0, 1.4)
serbiaDefensiveQDist = QualityDistribution(1.9, 1.4)

englandOffensiveQDist = QualityDistribution(2.7, 1.1)
englandDefensiveQDist = QualityDistribution(0.8, 1.3)

slovenia = Team("Slovenia", [], sloveniaOffensiveQDist, sloveniaDefensiveQDist)
denmark= Team("Denmark", [], denmarkOffensiveQDist, denmarkDefensiveQDist)
serbia = Team("Serbia", [], serbiaOffensiveQDist, serbiaDefensiveQDist)
england = Team("England", [], englandOffensiveQDist, englandDefensiveQDist)

polandOffensiveQDist = QualityDistribution(1.3, 1.4)
polandDefensiveQDist = QualityDistribution(1.4, 1.2)

netherlandsOffensiveQDist = QualityDistribution(1.9, 1.1)
netherlandsDefensiveQDist = QualityDistribution(1.3, 1.3)

austriaOffensiveQDist = QualityDistribution(1.5, 1.4)
austriaDefensiveQDist = QualityDistribution(1.4, 1.4)

franceOffensiveQDist = QualityDistribution(3.1, 1.1)
franceDefensiveQDist = QualityDistribution(0.8, 1.3)

poland = Team("Poland", [], polandOffensiveQDist, polandDefensiveQDist)
netherlands= Team("Netherlands", [], netherlandsOffensiveQDist, netherlandsDefensiveQDist)
austria = Team("Austria", [], austriaOffensiveQDist, austriaDefensiveQDist)
france = Team("France", [], franceOffensiveQDist, franceDefensiveQDist)

belgiumOffensiveQDist = QualityDistribution(2.9, 1.6)
belgiumDefensiveQDist = QualityDistribution(1.4, 1.6)

slovakiaOffensiveQDist = QualityDistribution(1.1, 1.1)
slovakiaDefensiveQDist = QualityDistribution(1.6, 1.3)

romaniaOffensiveQDist = QualityDistribution(1.3, 1.4)
romaniaDefensiveQDist = QualityDistribution(1.5, 1.4)

ukraineOffensiveQDist = QualityDistribution(1.2, 1.1)
ukraineDefensiveQDist = QualityDistribution(1.6, 1.3)

belgium = Team("Belgium", [], belgiumOffensiveQDist, belgiumDefensiveQDist)
slovakia= Team("Slovakia", [], slovakiaOffensiveQDist, slovakiaDefensiveQDist)
romania = Team("Romania", [], romaniaOffensiveQDist, romaniaDefensiveQDist)
ukraine = Team("Ukraine", [], ukraineOffensiveQDist, ukraineDefensiveQDist)

turkeyOffensiveQDist = QualityDistribution(1.3, 1.2)
turkeyDefensiveQDist = QualityDistribution(1.5, 1.7)

georgiaOffensiveQDist = QualityDistribution(0.4, 1.1)
georgiaDefensiveQDist = QualityDistribution(2.9, 1.3)

portugalOffensiveQDist = QualityDistribution(2.9, 1.2)
portugalDefensiveQDist = QualityDistribution(0.5, 1.4)

czechiaOffensiveQDist = QualityDistribution(1.6, 1.2)
czechiaDefensiveQDist = QualityDistribution(1.5, 1.4)

turkey = Team("Turkey", [], turkeyOffensiveQDist, turkeyDefensiveQDist)
georgia= Team("Georgia", [], georgiaOffensiveQDist, georgiaDefensiveQDist)
portugal = Team("Portugal", [], portugalOffensiveQDist, portugalDefensiveQDist)
czechia = Team("Czechia", [], czechiaOffensiveQDist, czechiaDefensiveQDist)

teams_dict = {"Germany": germany, "Switzerland": switzerland, "Scotland": scotland, "Hungary": hungary, "Spain": spain, "Italy": italy, "Croatia": croatia, "Albania": albania, "England": england,
              "Slovenia": slovenia, "Serbia": serbia, "Denmark": denmark, "France": france, "Netherlands": netherlands, "Poland": poland, "Austria": austria, "Belgium": belgium, "Slovakia": slovakia,
              "Romania": romania, "Ukraine": ukraine, "Turkey": turkey, "Portugal": portugal, "Czechia": czechia, "Georgia": georgia}

team_columns = ['overall', 'potential', 'pace', 'shooting', 'passing', 'dribbling',
                                'defending', 'physic', 'attacking_crossing', 'attacking_finishing',
                                'attacking_heading_accuracy', 'attacking_short_passing',
                                'attacking_volleys', 'skill_dribbling', 'skill_curve',
                                'skill_fk_accuracy', 'skill_long_passing', 'skill_ball_control',
                                'movement_acceleration', 'movement_sprint_speed', 'movement_agility',
                                'movement_reactions', 'movement_balance', 'power_shot_power',
                                'power_jumping', 'power_stamina', 'power_strength', 'power_long_shots',
                                'mentality_aggression', 'mentality_interceptions',
                                'mentality_positioning', 'mentality_vision', 'mentality_penalties',
                                'mentality_composure', 'defending_marking_awareness',
                                'defending_standing_tackle', 'defending_sliding_tackle',
                                'goalkeeping_diving', 'goalkeeping_handling', 'goalkeeping_kicking',
                                'goalkeeping_positioning', 'goalkeeping_reflexes', 'goalkeeping_speed']
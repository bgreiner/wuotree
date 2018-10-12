from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'sim_price_comp',
        'display_name': "Simultaneous price competition",
        'num_demo_participants': 5,
        'description' : "Quick convergence to lowest prices.",
        'behaviour' : """Strong forces of market competition, no room for cooperation.""",
        'app_sequence': ['ready', 'inputsecondid', 'sim_price_comp', 'thankyou'],
    },
    {
        'name': 'seq_price_comp',
        'display_name': "Sequential price competition",
        'num_demo_participants': 5,
        'app_sequence': ['ready', 'inputsecondid', 'seq_price_comp', 'thankyou'],
    },
    {
        'name': 'monopoly',
        'display_name': "Monopoly",
        'num_demo_participants': 6,
        'app_sequence': ['ready', 'inputsecondid', 'monopoly', 'thankyou'],
    },
    {
        'name': 'stack_comp',
        'display_name': "Stackelberg competition",
        'num_demo_participants': 2,
        'app_sequence': ['ready', 'inputsecondid', 'stack_comp', 'thankyou'],
    },
    {
        'name': 'stack_comp_rev',
        'display_name': "Stackelberg competition with revision option",
        'num_demo_participants': 2,
        'app_sequence': ['ready', 'inputsecondid', 'stack_comp_rev', 'thankyou'],
    },
    {
        'name': 'price_match',
        'display_name': "Price matching policies in Bertrand competition",
        'num_demo_participants': 5,
        'app_sequence': ['ready', 'inputsecondid', 'price_match', 'thankyou'],
    },
    {
        'name': 'dictator_game',
        'display_name': "Dictator Game",
        'num_demo_participants': 2,
        'app_sequence': ['ready', 'inputsecondid', 'dictator_game', 'thankyou'],
    },
    {
        'name': 'ultimatum_game',
        'display_name': "Ultimatum Game",
        'num_demo_participants': 2,
        'app_sequence': ['ready', 'inputsecondid', 'ultimatum_game', 'thankyou'],
    },
    {
        'name': 'ultimatum_game_rep',
        'display_name': "Repeated Ultimatum Game",
        'num_demo_participants': 2,
        'app_sequence': ['ready', 'inputsecondid', 'ultimatum_game_rep', 'thankyou'],
    },
    {
        'name': 'market_game',
        'display_name': "Market Game (2 proposers, 1 responder)",
        'num_demo_participants': 3,
        'app_sequence': ['ready', 'inputsecondid', 'market_game', 'thankyou'],
    },
    {
        'name': 'centipede_game',
        'display_name': "Centipede Game",
        'num_demo_participants': 2,
        'app_sequence': ['ready', 'inputsecondid', 'centipede_game', 'thankyou'],
    },
    {
        'name': 'infinite_prison',
        'display_name': "Infinitely Repeated Prisoners Dilemma",
        'num_demo_participants': 2,
        'num_rounds': 10,
        'app_sequence': ['ready', 'inputsecondid', 'infinite_prison', 'thankyou'],
    },
    {
        'name': 'finite_prison',
        'display_name': "Finitely Repeated Prisoners Dilemma",
        'num_demo_participants': 2,
        'num_rounds': 10,
        'app_sequence': ['ready', 'inputsecondid', 'finite_prison', 'thankyou'],
    },
    {
        'name': 'finite_prison_stranger',
        'display_name': "Finitely Repeated PD strangers",
        'num_demo_participants': 2,
        'num_rounds': 10,
        'app_sequence': ['ready', 'inputsecondid', 'finite_prison_stranger', 'thankyou'],
    },
    {
        'name': 'chain_store',
        'display_name': "Chain Store Game",
        'num_demo_participants': 2,
        'app_sequence': ['ready', 'inputsecondid', 'chain_store', 'thankyou'],
    },
    {
        'name': 'rep_trust',
        'display_name': "Repeated Trust Game - Strangers",
        'num_demo_participants': 2,
        'app_sequence': ['ready', 'inputsecondid', 'rep_trust', 'thankyou'],
    },
    {
        'name': 'rep_trust_reputation',
        'display_name': "Repeated Trust Game - Strangers with reputation",
        'num_demo_participants': 2,
        'app_sequence': ['ready', 'inputsecondid', 'rep_trust_reputation', 'thankyou'],
    },
    {
        'name': 'rep_trust_partner',
        'display_name': "Repeated Trust Game - Partners",
        'num_demo_participants': 2,
        'app_sequence': ['ready', 'inputsecondid', 'rep_trust_partner', 'thankyou'],
    },
    {
        'name': 'japanese_auction',
        'display_name': 'Japanese Auction',
        'num_demo_participants': 4,
        'app_sequence': ['ready', 'inputsecondid', 'japanese_auction', 'thankyou'],
    },
    {
        'name': 'english_auction',
        'display_name': 'English Auction',
        'num_demo_participants': 4,
        'app_sequence': ['ready', 'inputsecondid', 'english_auction', 'thankyou'],
    },
    {
        'name': 'dutch_auction',
        'display_name': 'Dutch Auction',
        'num_demo_participants': 4,
        'app_sequence': ['ready', 'inputsecondid', 'dutch_auction', 'thankyou'],
    },
    {
        'name': 'first_price_auction',
        'display_name': '1st-price Sealed-bid Auction',
        'num_demo_participants': 4,
        'app_sequence': ['ready', 'inputsecondid', 'first_price_auction', 'thankyou'],
    },
    {
        'name': 'second_price_auction',
        'display_name': '2nd-price Sealed-bid Auction',
        'num_demo_participants': 4,
        'app_sequence': ['ready', 'inputsecondid', 'second_price_auction', 'thankyou'],
    },
    {
        'name': 'minimum_game',
        'display_name': 'Minimum (weakest link) game',
        'num_demo_participants': 6,
        'app_sequence': ['ready', 'inputsecondid', 'minimum_game', 'thankyou'],
    },
    {
        'name': 'coordination_games',
        'display_name': '6 little coordination games',
        'num_demo_participants': 2,
        'app_sequence': ['ready', 'inputsecondid', 'coord1', 'coord2', 'coord3', 'coord4', 'coord5', 'coord6',
                         'thankyou'],
        'poss_payoff': 10,
        'pot': 100,
    },
    {
        'name': 'battle_sexes',
        'display_name': 'Battle of the Sexes',
        'num_demo_participants': 2,
        'app_sequence': ['ready', 'inputsecondid', 'battle_sexes', 'thankyou'],
        'male_role': 'Football',
        'fem_role': 'Opera'
    },
    {
        'name': 'chicken',
        'display_name': 'Chicken',
        'num_demo_participants': 2,
        'app_sequence': ['ready', 'inputsecondid', 'chicken', 'thankyou'],
    },
    {
        'name': 'hermit',
        'display_name': 'The Hermit and the Socialiser',
        'num_demo_participants': 2,
        'app_sequence': ['ready', 'inputsecondid', 'hermit', 'thankyou'],
    },
    {
        'name': 'job_market',
        'display_name': 'Job Market Game (without signalling)',
        'num_demo_participants': 2,
        'app_sequence': ['ready', 'inputsecondid', 'job_market', 'thankyou'],
    },
    {
        'name': 'job_market_signal',
        'display_name': 'Job Market Game (with signalling)',
        'num_demo_participants': 2,
        'app_sequence': ['ready', 'inputsecondid', 'job_market_signal', 'thankyou'],
    },
    {
        'name': 'information_cascade',
        'display_name': 'Information Cascade',
        'num_demo_participants': 6,
        'app_sequence': ['ready', 'inputsecondid', 'information_cascade', 'thankyou'],
        'no_of_groups': 2,
    },
    {
        'name': 'rep_price_comp',
        'display_name': 'Repeated Price Comp',
        'num_demo_participants': 2,
        'app_sequence': ['ready', 'inputsecondid', 'rep_price_comp', 'thankyou'],
    },
    {
        'name': 'public_goods',
        'display_name': 'Public Goods',
        'num_demo_participants': 3,
        'app_sequence': ['ready', 'inputsecondid', 'public_goods', 'thankyou'],
    },
    {
        'name': 'public_goods_cond',
        'display_name': 'Public Goods with Condition Strategies',
        'num_demo_participants': 4,
        'app_sequence': ['ready', 'inputsecondid', 'public_goods_cond', 'thankyou'],
    },
    {
        'name': 'public_goods_punish',
        'display_name': 'Public Goods with Punishment',
        'num_demo_participants': 4,
        'app_sequence': ['ready', 'inputsecondid', 'public_goods_punish', 'thankyou'],
    },
    {
        'name': 'dutch',
        'display_name': "Dutch Auction version 2",
        'num_demo_participants': 4,
        'app_sequence': ['ready', 'inputsecondid', 'dutch', 'thankyou'],
    },
    {
        'name': 'japanese',
        'display_name': "Japanese Auction version 2",
        'num_demo_participants': 4,
        'app_sequence': ['ready', 'inputsecondid', 'japanese', 'thankyou'],
    },
    {
        'name': 'vendora',
        'display_name': "Newsvendor A",
        'num_demo_participants': 4,
        'app_sequence': ['ready', 'vendora', 'thankyou'],
    },
    {
        'name': 'random_hermits',
        'display_name': "Random Hermits",
        'num_demo_participants': 2,
        'app_sequence': ['ready', 'inputsecondid', 'random_hermits', 'thankyou'],
    },
    {
        'name': 'penaltykick',
        'display_name': "Penalty Kick",
        'num_demo_participants': 2,
        'app_sequence': ['ready', 'inputsecondid', 'penalty_kick', 'thankyou'],
    },
    {
        'name': 'penaltykickbri',
        'display_name': "Penalty Kick Bribery",
        'num_demo_participants': 2,
        'app_sequence': ['ready', 'inputsecondid', 'penalty_kick_bribery', 'thankyou'],
    },
    {
        'name': 'marketentry',
        'display_name': "Market Entry",
        'num_demo_participants': 2,
        'app_sequence': ['ready', 'inputsecondid', 'market_entry', 'thankyou'],
    },
    {
        'name': 'agenda1',
        'display_name': "Agenda Setting 1",
        'num_demo_participants': 2,
        'app_sequence': ['ready', 'inputsecondid', 'agenda_1', 'thankyou'],
    },
    {
        'name': 'agenda2',
        'display_name': "Agenda Setting 2",
        'num_demo_participants': 3,
        'app_sequence': ['ready', 'inputsecondid', 'agenda_2', 'thankyou'],
    },


]
# see the end of this file for the inactive session configs


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    {
        'name': 'manec_securelabels',
        'display_name': 'Managerial Economics (GREINER)',
        'participant_label_file': '_rooms/ManEcon_GREINER.txt',
        'use_secure_urls': True
    },
    {
        'name': 'strategy_1',
        'display_name': 'Strategy 1',
        'participant_label_file': '_rooms/strategy_1.txt',
        'use_secure_urls': True
    },
    {
        'name': 'strategy_2',
        'display_name': 'Strategy 2',
        'participant_label_file': '_rooms/strategy_1.txt',
        'use_secure_urls': True
    },
    {
        'name': 'emp_analysis',
        'display_name': 'Empirical Data and Analysis II',
    },
    {
        'name': 'live_demo',
        'display_name': 'Live Demo',
    },
]



# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


# Consider '', None, and '0' to be empty/false
#DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})
#DEBUG = True
DEBUG = True

DEMO_PAGE_INTRO_HTML = """
Here are various games implemented with 
oTree. These games are open
source, and you can modify them as you wish.
"""

USE_POINTS = True
POINTS_DECIMAL_PLACES = 2
POINTS_CUSTOM_NAME = 'E$' 

# don't share this with anybody.
SECRET_KEY = 'gd-*23s30&z)@4cxn#7hilnm)x%n)_xrx@r^vbl*3bo#alx%gk'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# inactive session configs
### {
###     'name': 'trust',
###     'display_name': "Trust Game",
###     'num_demo_participants': 2,
###     'app_sequence': ['trust', 'payment_info'],
### },
### {
###     'name': 'prisoner',
###     'display_name': "Prisoner's Dilemma",
###     'num_demo_participants': 2,
###     'app_sequence': ['prisoner', 'payment_info'],
### },
### {
###     'name': 'ultimatum',
###     'display_name': "Ultimatum (randomized: strategy vs. direct response)",
###     'num_demo_participants': 2,
###     'app_sequence': ['ultimatum', 'payment_info'],
### },
### {
###     'name': 'ultimatum_strategy',
###     'display_name': "Ultimatum (strategy method treatment)",
###     'num_demo_participants': 2,
###     'app_sequence': ['ultimatum', 'payment_info'],
###     'use_strategy_method': True,
### },
### {
###     'name': 'ultimatum_non_strategy',
###     'display_name': "Ultimatum (direct response treatment)",
###     'num_demo_participants': 2,
###     'app_sequence': ['ultimatum', 'payment_info'],
###     'use_strategy_method': False,
### },
### {
###     'name': 'vickrey_auction',
###     'display_name': "Vickrey Auction",
###     'num_demo_participants': 3,
###     'app_sequence': ['vickrey_auction', 'payment_info'],
### },
### {
###     'name': 'volunteer_dilemma',
###     'display_name': "Volunteer's Dilemma",
###     'num_demo_participants': 3,
###     'app_sequence': ['volunteer_dilemma', 'payment_info'],
### },
### {
###     'name': 'cournot',
###     'display_name': "Cournot Competition",
###     'num_demo_participants': 2,
###     'app_sequence': [
###         'cournot', 'payment_info'
###     ],
### },
### {
###     'name': 'principal_agent',
###     'display_name': "Principal Agent",
###     'num_demo_participants': 2,
###     'app_sequence': ['principal_agent', 'payment_info'],
### },
### {
###     'name': 'dictator',
###     'display_name': "Dictator Game",
###     'num_demo_participants': 2,
###     'app_sequence': ['dictator', 'payment_info'],
### },
### {
###     'name': 'matching_pennies',
###     'display_name': "Matching Pennies",
###     'num_demo_participants': 2,
###     'app_sequence': [
###         'matching_pennies',
###     ],
### },
### {
###     'name': 'traveler_dilemma',
###     'display_name': "Traveler's Dilemma",
###     'num_demo_participants': 2,
###     'app_sequence': ['traveler_dilemma', 'payment_info'],
### },
### {
###     'name': 'bargaining',
###     'display_name': "Bargaining Game",
###     'num_demo_participants': 2,
###     'app_sequence': ['bargaining', 'payment_info'],
### },
### {
###     'name': 'common_value_auction',
###     'display_name': "Common Value Auction",
###     'num_demo_participants': 3,
###     'app_sequence': ['common_value_auction', 'payment_info'],
### },
### {
###     'name': 'bertrand',
###     'display_name': "Bertrand Competition",
###     'num_demo_participants': 2,
###     'app_sequence': [
###         'bertrand', 'payment_info'
###     ],
### },
### {
###     'name': 'real_effort',
###     'display_name': "Real-effort transcription task",
###     'num_demo_participants': 1,
###     'app_sequence': [
###         'real_effort',
###     ],
### },
### {
###     'name': 'lemon_market',
###     'display_name': "Lemon Market Game",
###     'num_demo_participants': 3,
###     'app_sequence': [
###         'lemon_market', 'payment_info'
###     ],
### },
### {
###     'name': 'public_goods_simple',
###     'display_name': "Public Goods (simple version from tutorial)",
###     'num_demo_participants': 3,
###     'app_sequence': ['public_goods_simple', 'payment_info'],
### },
### {
###     'name': 'trust_simple',
###     'display_name': "Trust Game (simple version from tutorial)",
###     'num_demo_participants': 2,
###     'app_sequence': ['trust_simple'],
### },

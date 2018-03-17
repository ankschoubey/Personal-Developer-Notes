from django.shortcuts import render
import json
from django.http import HttpResponse

# Create your views here.

data = {
    "Recommended for you": [
        252,
        253,
        255,
        256,
        257,
        259,
        261,
        264,
        265,
        266,
        267,
        269,
        270,
        502,
        503,
        504,
        506,
        507,
        508,
        518,
        532,
        670,
        2356,
        2693,
        3238,
        3265,
        3542,
        3547,
        3563,
        3565,
        3603,
        3978,
        3994,
        3999,
        4039,
        4040,
        4077,
        4088,
        4092,
        4094,
        4280,
        4341,
        4342,
        4346,
        4347,
        4353,
        4381,
        4384,
        4402,
        4821,
        4824,
        4828,
        5471,
        5473,
        5707,
        5915,
        6190,
        7400,
        8312,
        8320,
        8324
    ],
    "Because you liked Destiny Turns on the Radio ": [
        5915,
        7400,
        4828,
        8324,
        518,
        8320,
        4077,
        3238,
        4088,
        8312,
        4092,
        4824,
        4094,
        4821,
        2356,
        6190,
        3265,
        532,
        5707,
        5471,
        5473
    ],
    "User who liked Destiny Turns on the Radio also liked this": [
        670,
        270,
        269,
        503,
        267,
        266,
        265,
        264,
        504,
        506,
        502,
        261,
        259,
        507,
        257,
        256,
        255,
        508,
        253,
        252
    ],
    "movies": {
        "256": {
            "id": "256",
            "title": "Beyond Bedlam",
            "overview": "An experiment gone awry places a neurologist (Elizabeth Hurley) and a homicide detective (Craig Fairbrass) in a psychopath's (Keith Allen) nightmarish world.",

            "poster": "movie_images/poster/256.png",
            "video": 0
        },
        "257": {
            "id": "257",
            "title": "Nina Takes a Lover",
            "overview": "Laura San Giacomo stars in this sexy comedy about adultery. When Nina's (San Giacomo) husband goes out of town for several weeks on a business trip, Nina hooks up with a photographer. Told from a reporter's point of view, his interviews with Nina and the photographer provide comic insights. Stars Laura San Giacomo, Paul Rhys, Michael O'Keefe, Fisher Stevens and more.",
            "backdrop": "movie_images/backdrop/257.png",
            "poster": "movie_images/poster/257.png",
            "video": 0
        },
        "4353": {
            "id": "4353",
            "title": "True Confessions",
            "overview": "A cop clashes with his priest brother while investigating the brutal murder of a young prostitute",
            "backdrop": "movie_images/backdrop/4353.png",
            "poster": "movie_images/poster/4353.png",
            "video": 0
        },
        "259": {
            "id": "259",
            "title": "Only You",
            "overview": "A childhood incident has convinced Faith Corvatch that her true love is a guy named \"Damon Bradley,\" but she has yet to meet him. Preparing to settle down and marry a foot doctor, Faith impulsively flies to Venice when it seems that she may be able to finally encounter the man of her dreams. Instead, she meets the charming Peter Wright. But can they fall in love if she still believes that she is intended to be with someone else?",
            "backdrop": "movie_images/backdrop/259.png",
            "poster": "movie_images/poster/259.png",
            "video": 0
        },
        "8320": {
            "id": "8320",
            "title": "The Internship",
            "overview": "Two recently laid-off men in their 40s try to make it as interns at a successful Internet company where their managers are in their 20s.",
            "backdrop": "movie_images/backdrop/8320.png",
            "poster": "movie_images/poster/8320.png",
            "video": 0
        },
        "261": {
            "id": "261",
            "title": "Poison Ivy II: Lily",
            "overview": "A young and naive college art student becomes obsessed with assuming the identity and personality of a departed coed who used to live in her room, and in so doing causes complications that result in two men, a student and her art professor, lusting after her.",
            "backdrop": "movie_images/backdrop/261.png",
            "poster": "movie_images/poster/261.png",
            "video": 0
        },
        "518": {
            "id": "518",
            "title": "The Brady Bunch Movie",
            "overview": "The original 70's TV family is now placed in the 1990's, where they're even more square and out of place than ever.",
            "backdrop": "movie_images/backdrop/518.png",
            "poster": "movie_images/poster/518.png",
            "video": 0
        },
        "2693": {
            "id": "2693",
            "title": "Betrayed",
            "overview": "An FBI agent (Debra Winger) falls in love with a white supremacist (Tom Berenger) whose group she infiltrates.",
            "backdrop": "movie_images/backdrop/2693.png",
            "poster": "movie_images/poster/2693.png",
            "video": 0
        },
        "264": {
            "id": "264",
            "title": "The Perez Family",
            "overview": "In the midst of the Mariel boat lift -- a hurried exodus of refugees from Cuba going to America -- an immigration clerk accidentally presumes that dissident Juan Raul Perez and Dorita Evita Perez are married. United by their last name and a mutual resolve to emigrate, Dorita and Juan agree to play along. But it gets complicated when the two begin falling for each other just as Juan reunites with his wife, Carmela, whom he hasn't seen in decades.",
            "backdrop": "movie_images/backdrop/264.png",
            "poster": "movie_images/poster/264.png",
            "video": 0
        },
        "265": {
            "id": "265",
            "title": "A Pyromaniac's Love Story",
            "overview": "A pastry boy and the son of a hair-piece mogul become involved in an arson scandal. Sergio is offered a bribe in exchange for taking the blame for the fire that destroys his workplace. Garet, the real arsonist, is apalled that someone else would try to take credit for his act of love. Before long, Sergio and Garet become entangled in a zany love-quadrangle involving Hattie and Stephanie. Written by Brian Whiting",

            "poster": "movie_images/poster/265.png",
            "video": 0
        },
        "266": {
            "id": "266",
            "title": "Pulp Fiction",
            "overview": "A burger-loving hit man, his philosophical partner, a drug-addled gangster's moll and a washed-up boxer converge in this sprawling, comedic crime caper. Their adventures unfurl in three stories that ingeniously trip back and forth in time.",
            "backdrop": "movie_images/backdrop/266.png",
            "poster": "movie_images/poster/266.png",
            "video": 0
        },
        "267": {
            "id": "267",
            "title": "Priest",
            "overview": "Father Greg Pilkington (Linus Roache) is torn between his call as a conservative Catholic priest and his secret life as a homosexual with a gay lover, frowned upon by the Church. Upon hearing the confession of a young girl of her incestuous father, Greg enters an intensely emotional spiritual struggle deciding between choosing morals over religion and one life over another.",
            "backdrop": "movie_images/backdrop/267.png",
            "poster": "movie_images/poster/267.png",
            "video": 0
        },
        "3978": {
            "id": "3978",
            "title": "Intersection",
            "overview": "During a car accident, Vincent Eastman watches his whole life flash before his eyes, and he doesn't like what he sees. While maintaining the semblance of a marriage with his wife, Sally, Vincent has been carrying on with a mistress, Olivia. She's everything Sally isn't -- warm, passionate, carefree. So why can't he choose between the two, especially when his indecision is taking its toll on his daughter?",
            "backdrop": "movie_images/backdrop/3978.png",
            "poster": "movie_images/poster/3978.png",
            "video": 0
        },
        "269": {
            "id": "269",
            "title": "Picture Bride",
            "overview": "Riyo, an orphaned 17-year old, sails from Yokohama to Hawaii in 1918 to marry Matsuji, a man she has never met. Hoping to escape a troubled past and start anew, Riyo is bitterly disappointed upon her arrival: her husband is twice her age. The miserable girl finds solace with her new friend Kana, a young mother who helps Riyo accept her new life.",
            "backdrop": "movie_images/backdrop/269.png",
            "poster": "movie_images/poster/269.png",
            "video": 0
        },
        "270": {
            "id": "270",
            "title": "Queen Margot",
            "overview": "The night of August 24, 1572, is known as the Massacre of St. Bartholomew. In France a religious war is raging. In order to impose peace a forced wedding is arranged between Margot de Valois, sister of the immature Catholic King Charles IX, and the Hugenot King Henri of Navarre. Catherine of Medici maintains her behind-the-scenes power by ordering assaults, poisonings, and instigations to incest.",
            "backdrop": "movie_images/backdrop/270.png",
            "poster": "movie_images/poster/270.png",
            "video": 0
        },
        "3603": {
            "id": "3603",
            "title": "Blaze",
            "overview": "This movie tells the story of the latter years of Earl Long, a flamboyant governor of Louisiana. The aging Earl, an unapologetic habitue of strip joints, falls in love with young stripper Blaze Starr. When Earl and Blaze move in together, Earl's opponents use this to attack his controversial political program, which included civil rights for blacks in the 1950's.",
            "backdrop": "movie_images/backdrop/3603.png",
            "poster": "movie_images/poster/3603.png",
            "video": 0
        },
        "532": {
            "id": "532",
            "title": "Bye Bye Love",
            "overview": "With varying degrees of success, recently divorced friends Dave, Vic and Donny are trying to move on with their lives. Vic feels vilified by his ex-wife's parents, while Donny has a shaky bond with his teen daughter, Emma. Dave, meanwhile, has an enviable problem -- he has more dates than he can handle. As they confront their post-marital challenges, the men take solace in one another's plights.",
            "backdrop": "movie_images/backdrop/532.png",
            "poster": "movie_images/poster/532.png",
            "video": 0
        },
        "8324": {
            "id": "8324",
            "title": "The Hangover Part III",
            "overview": "This time, there's no wedding. No bachelor party. What could go wrong, right? But when the Wolfpack hits the road, all bets are off.",
            "backdrop": "movie_images/backdrop/8324.png",
            "poster": "movie_images/poster/8324.png",
            "video": 0
        },
        "3994": {
            "id": "3994",
            "title": "The Long Good Friday",
            "overview": "In the late 1970s, Cockney crime boss Harold Shand, a gangster trying to become a legitimate property mogul, has big plans to get the American Mafia to bankroll his transformation of a derelict area of London into the possible venue for a future Olympic Games. However, a series of bombings targets his empire on the very weekend the Americans are in town. Shand is convinced there is a traitor in his organization, and sets out to eliminate the rat in typically ruthless fashion.",
            "backdrop": "movie_images/backdrop/3994.png",
            "poster": "movie_images/poster/3994.png",
            "video": 0
        },
        "5915": {
            "id": "5915",
            "title": "Waterboys",
            "overview": "In a Japanese school, 5 adolescent geeks join the new sport teacher and take up the challenge to take part in the synchronised swimming competition, in-spite of the mockeries of the \"real sportsmen\".",
            "backdrop": "movie_images/backdrop/5915.png",
            "poster": "movie_images/poster/5915.png",
            "video": 0
        },
        "4381": {
            "id": "4381",
            "title": "Best Friends",
            "overview": "When a professional couple who have lived &amp; worked together for many years finally decide to marry, their sudden betrothal causes many unexpectedly funny and awkward difficulties. They soon find that being married is often quite different from being \"best friends.\"",
            "backdrop": "movie_images/backdrop/4381.png",
            "poster": "movie_images/poster/4381.png",
            "video": 0
        },
        "670": {
            "id": "670",
            "title": "Kaspar Hauser",
            "overview": "No overview found.",
            "backdrop": "movie_images/backdrop/670.png",
            "poster": "movie_images/poster/670.png",
            "video": 0
        },
        "3999": {
            "id": "3999",
            "title": "The Ninth Configuration",
            "overview": "Col. Vincent Kane is a military psychiatrist who takes charge of an army mental hospital situated in a secluded castle. Among Kane's many eccentric patients is Capt. Billy Cutshaw, a troubled astronaut in the midst of an existential crisis. Although Kane's own grasp on sanity is questionable, he manages to engage Cutshaw in a series of thoughtful conversations about science and faith that deeply affect the lives of both men.",
            "backdrop": "movie_images/backdrop/3999.png",
            "poster": "movie_images/poster/3999.png",
            "video": 0
        },
        "4384": {
            "id": "4384",
            "title": "Cannery Row",
            "overview": "A depressed section of Monterey, California is the backdrop for an offbeat romantic comedy about a pair of mismatched lovers. Doc is a lonely marine biologist and former baseball star. Suzy is a scrappy, abrasive drifter who can't even succeed as a prostitute. Add Cannery Row's band of resident drunken derelicts to the mix and fireworks result, though not the romantic kind.",
            "backdrop": "movie_images/backdrop/4384.png",
            "poster": "movie_images/poster/4384.png",
            "video": 0
        },
        "3238": {
            "id": "3238",
            "title": "Don't Tell Mom the Babysitter's Dead",
            "overview": "Sue Ellen Crandell is a teenager eagerly awaiting her mother's summer-long absence. While the babysitter looks after her rambunctious younger siblings, Sue Ellen can party and have fun. But then the babysitter abruptly dies, leaving the Crandells short on cash. Sue Ellen finds a sweet job in fashion by lying about her age and experience on her r\u00e9sum\u00e9. But, while her siblings run wild, she discovers the downside of adulthood",
            "backdrop": "movie_images/backdrop/3238.png",
            "poster": "movie_images/poster/3238.png",
            "video": 0
        },
        "6190": {
            "id": "6190",
            "title": "Georgy Girl",
            "overview": "Georgy has resigned herself to being one of life's accidents. She disapproves somewhat of her father's butlering James Leamington. She's tall, plump, sloppy and wistfully envious of what she conceives to be the life led by her beautiful, but icy roommate. Where her roommate, Meredith, is cool and calculating, Georgy gets so involved with the people around her she behaves like an affectionate puppy. Most of all she burns to be a mother. But it is Meredith that is in the hospital having an unwanted child.",
            "backdrop": "movie_images/backdrop/6190.png",
            "poster": "movie_images/poster/6190.png",
            "video": 0
        },
        "4402": {
            "id": "4402",
            "title": "Bad Influence",
            "overview": "Michael, a wimpy young executive, is about to get pulverized by a jealous boyfriend in a bar when a handsome, mysterious stranger steps in--and then disappears. Later that night, while jogging, Michael runs into the stranger on a pier. He introduces himself as Alex, and the two go out to an under- ground club. Alex wheedles his way into Michael's life and turns it upside down...",
            "backdrop": "movie_images/backdrop/4402.png",
            "poster": "movie_images/poster/4402.png",
            "video": 0
        },
        "2356": {
            "id": "2356",
            "title": "The Palm Beach Story",
            "overview": "Gerry and Tom Jeffers are finding married life hard. Tom is an inventor/ architect and there is little money for them to live on. They are about to be thrown out of their apartment when Gerry meets rich businessman being shown around as a prospective tenant. He gives Gerry $700 to start life afresh but Tom refuses to believe her story and they quarrel. Gerry decides the marriage is over and heads to Palm Beach for a quick divorce but Tom has plans to stop her.",
            "backdrop": "movie_images/backdrop/2356.png",
            "poster": "movie_images/poster/2356.png",
            "video": 0
        },
        "4280": {
            "id": "4280",
            "title": "Wholly Moses",
            "overview": "Harvey and Zoey, two tourists in Israel, discover an ancient scroll about Herschel, the man who was almost Moses. Herschel receives the command from God to free his people from slavery, but Moses keeps getting all the credit.",
            "backdrop": "movie_images/backdrop/4280.png",
            "poster": "movie_images/poster/4280.png",
            "video": 0
        },
        "3265": {
            "id": "3265",
            "title": "Back to the Beach",
            "overview": "Cowabunga! The surfing '60s ride into the new wave as Frankie and Annette star in this hip update of their old-time, good-time beach movies. With special appearances by Bob Denver, Tony Dow, Pee-Wee Herman, Jerry Mathers and other familiar faces. Frankie and Annette grow up and have kids in the midwest. They return to LA to visit their daughter who is shacked up with her boyfriend and tries to hide the fact. They begin to have marriage problems when Frankie runs into Connie, who has erected a shrine to him in her night club. Their punk son has joined up with the local surf toughs, and things all come to a head when the toughs challenge the good guys to a surfing duel",
            "backdrop": "movie_images/backdrop/3265.png",
            "poster": "movie_images/poster/3265.png",
            "video": 0
        },
        "4039": {
            "id": "4039",
            "title": "Crimes of Passion",
            "overview": "Joanna Crane lives a double life. During the day she works as fashion designer but during the night she is the high class prostitute China Blue. As she is accused for industrial spying, Bobby Grady is hired to shadow her. However, they fall in love.  Meanwhile a psychopathic preacher starts stalking her.",
            "backdrop": "movie_images/backdrop/4039.png",
            "poster": "movie_images/poster/4039.png",
            "video": 0
        },
        "4040": {
            "id": "4040",
            "title": "The Evil That Men Do",
            "overview": "Professional killer Holland is forced out of retirement to break a Central American government's political torture ring when one of his friends, a Latin American journalist, is killed. The murderer, Doctor Clement Molloch, is the master sadist behind the political torture of innocent victims. Posing as a journalist, Holland lures Molloch out of his fortress-like headquarters by using his murdered friend's wife and daughter as bait. When Holland kidnaps Molloch's sister, the doctor is led on a wild chase that takes him to an abandoned opal mine where he finally comes face to face with Holland.",
            "backdrop": "movie_images/backdrop/4040.png",
            "poster": "movie_images/poster/4040.png",
            "video": 0
        },
        "5707": {
            "id": "5707",
            "title": "Unfaithfully Yours",
            "overview": "Sir Alfred De Carter suspects his wife of infidelity. While conducting a symphony orchestra, he imagines three different ways of dealing with the situation.",
            "backdrop": "movie_images/backdrop/5707.png",
            "poster": "movie_images/poster/5707.png",
            "video": 0
        },
        "4821": {
            "id": "4821",
            "title": "The Meaning of Life",
            "overview": "Life's questions are 'answered' in a series of outrageous vignettes, beginning with a staid London insurance company which transforms before our eyes into a pirate ship. Then there's the National Health doctors who try to claim a healthy liver from a still-living donor. The world's most voracious glutton brings the art of vomiting to new heights before his spectacular demise.",
            "backdrop": "movie_images/backdrop/4821.png",
            "poster": "movie_images/poster/4821.png",
            "video": 0
        },
        "3542": {
            "id": "3542",
            "title": "Criminal Law",
            "overview": "A rising young attorney successfully defends a man accused of murder, only to have the same type of murder then happen again. Right away the previously defended man hires the attorney again, and although the attorney is quite certain that he is the killer, he agrees to again defend him... much to the consternation of his friends. However, he explains that by being his attorney he will be better able to catch the man in a mistake... and on this the rest of the film develops, with the killer playing a cat and mouse game with the attorney until, at last, they both must recognize that they are not all that different.",
            "backdrop": "movie_images/backdrop/3542.png",
            "poster": "movie_images/poster/3542.png",
            "video": 0
        },
        "4088": {
            "id": "4088",
            "title": "Cactus Flower",
            "overview": "Distraught when her middle-aged lover breaks a date with her, 21-year-old Toni Simmons attempts suicide. Impressed by her action, her lover, dentist Julian Winston reconsiders marrying Toni, but he worries about her insistence on honesty. Having fabricated a wife and three children, Julian readily accepts when his devoted nurse, Stephanie, who has secretly loved Julian for years, offers to act as his wife and demand a divorce.",
            "backdrop": "movie_images/backdrop/4088.png",
            "poster": "movie_images/poster/4088.png",
            "video": 0
        },
        "4824": {
            "id": "4824",
            "title": "PCU",
            "overview": "Nervous high school senior Tom Lawrence visits Port Chester University, where he gets a taste of politically correct college life when he's guided by fraternity wild man Droz and his housemates at The Pit. But Droz and his pals have rivals in nasty preppy Rand McPherson and the school's steely president. With their house threatened with expulsion, Droz and company decide to throw a raging party where the various factions will collide.",
            "backdrop": "movie_images/backdrop/4824.png",
            "poster": "movie_images/poster/4824.png",
            "video": 0
        },
        "3547": {
            "id": "3547",
            "title": "The Dead Pool",
            "overview": "Dirty Harry Callahan returns for his final film adventure. Together with his partner Al Quan, he must investigate the systematic murder of actors and musicians. By the time Harry learns that the murders are a part of a sick game to predict the deaths of celebrities before they happen, it may be too late...",
            "backdrop": "movie_images/backdrop/3547.png",
            "poster": "movie_images/poster/3547.png",
            "video": 0
        },
        "4828": {
            "id": "4828",
            "title": "Three O'Clock High",
            "overview": "A high school nerd, Jerry Mitchell (Siemaszko) is assigned to write a piece for the school paper about new boy Buddy Revell (Tyson), who is rumored to be a psychopathic nutcase. When Jerry accidentally touches Buddy, he says that they must fight in the parking lot at 3pm. Jerry will just about do anything to avoid the confrontation",
            "backdrop": "movie_images/backdrop/4828.png",
            "poster": "movie_images/poster/4828.png",
            "video": 0
        },
        "8312": {
            "id": "8312",
            "title": "Bill Hicks: Revelations",
            "overview": "Since his untimely death from pancreatic cancer in 1994, Bill Hicks has become a comedy legend. Now fans who may have never had the opportunity to see his act live on-stage will finally be able to experience Hicks' unique and confrontational brand of comedy.",
            "backdrop": "movie_images/backdrop/8312.png",
            "poster": "movie_images/poster/8312.png",
            "video": 0
        },
        "5471": {
            "id": "5471",
            "title": "Our Hospitality",
            "overview": "A man returns to his Appalachian homestead. On the trip, he falls for a young woman. The only problem is her family has vowed to kill every member of his family.",
            "backdrop": "movie_images/backdrop/5471.png",
            "poster": "movie_images/poster/5471.png",
            "video": 0
        },
        "5473": {
            "id": "5473",
            "title": "The Farmer's Daughter",
            "overview": "A Swedish-American farmer's daughter leaves the farm to attend nursing school. Penny-less after an acquaintance steals her tuition money, she obtains a job as a household servant for congressman Glenn Morley where she finds politics and romance.",
            "backdrop": "movie_images/backdrop/5473.png",
            "poster": "movie_images/poster/5473.png",
            "video": 0
        },
        "7400": {
            "id": "7400",
            "title": "Old Dogs",
            "overview": "Charlie and Dan have been best friends and business partners for thirty years; their Manhattan public relations firm is on the verge of a huge business deal with a Japanese company. With two weeks to sew up the contract, Dan gets a surprise: a woman he married on a drunken impulse nearly nine years before (annulled the next day) shows up to tell him he's the father of her twins, now seven, and she'll be in jail for 14 days for a political protest. Dan volunteers to keep the tykes, although he's up tight and clueless. With Charlie's help is there any way they can be dad and uncle, meet the kids' expectations, and still land the account?",
            "backdrop": "movie_images/backdrop/7400.png",
            "poster": "movie_images/poster/7400.png",
            "video": 0
        },
        "4346": {
            "id": "4346",
            "title": "Sharky's Machine",
            "overview": "Sharky gets busted back to working vice, where he happens upon a scandalous conspiracy involving a local politician. Accompanied by an all-star jazz soundtrack, Sharky's new \"machine\" gathers evidence while Sharky falls in love with a woman he has never met.",
            "backdrop": "movie_images/backdrop/4346.png",
            "poster": "movie_images/poster/4346.png",
            "video": 0
        },
        "3563": {
            "id": "3563",
            "title": "Masquerade",
            "overview": "A recently orphaned millionairess, Olivia, really hates her scheming step-father. Olivia finds love with a young yacht racing captain, Tim, who isn't completely truthful with her. When the two run into a problem the local cop, who happens to be an old friend of Olivia's, seems to be turning a blind eye to incriminating evidence.",
            "backdrop": "movie_images/backdrop/3563.png",
            "poster": "movie_images/poster/3563.png",
            "video": 0
        },
        "4092": {
            "id": "4092",
            "title": "The Survivors",
            "overview": "Having both lost their jobs, two strangers become unlikely friends after a run in with a would be robber, who is actually a hitman with a grudge against the two.",
            "backdrop": "movie_images/backdrop/4092.png",
            "poster": "movie_images/poster/4092.png",
            "video": 0
        },
        "3565": {
            "id": "3565",
            "title": "Moon Over Parador",
            "overview": "Little known actor, Jack Noah, is working on location in the dictatorship of Parador at the time the dictator dies. The dictator's right hand man, Roberto, makes Jack an offer he cannot refuse.. to play the dictator. Jack's acting skills fool the masses but not close friends and employees of the dictator.",
            "backdrop": "movie_images/backdrop/3565.png",
            "poster": "movie_images/poster/3565.png",
            "video": 0
        },
        "4077": {
            "id": "4077",
            "title": "Delirious",
            "overview": "A soap opera writer gets hit on the head and wakes up as a character in his own show.",
            "backdrop": "movie_images/backdrop/4077.png",
            "poster": "movie_images/poster/4077.png",
            "video": 0
        },
        "4347": {
            "id": "4347",
            "title": "So Fine",
            "overview": "While trying to get his father out of a financial jam, a man comes up with an idea that turns into an unexpected overnight financial fashion success - the bottomless pants.",
            "backdrop": "movie_images/backdrop/4347.png",
            "poster": "movie_images/poster/4347.png",
            "video": 0
        },
        "252": {
            "id": "252",
            "title": "Murder in the First",
            "overview": "Inspired by a true story. A petty criminal sent to Alcatraz in the 1930s is caught attempting to make an escape. As punishment he is put in solitary confinement. The maximum stay is supposed to be 19 days, but Henri spends years alone, cold and in complete darkness, only to emerge a madman and soon to be a murderer. The story follows a rookie lawyer attempting to prove that Alcatraz was to blame.",
            "backdrop": "movie_images/backdrop/252.png",
            "poster": "movie_images/poster/252.png",
            "video": 0
        },
        "4341": {
            "id": "4341",
            "title": "Toy Soldiers",
            "overview": "After federal agents arrest a drug czar and put him on trial, the cartel leader's vicious son storms a prep school and takes its students hostage. They rebel against the armed intruders and try to take back their academy by any means necessary.",
            "backdrop": "movie_images/backdrop/4341.png",
            "poster": "movie_images/poster/4341.png",
            "video": 0
        },
        "502": {
            "id": "502",
            "title": "Killer",
            "overview": "This lyrical, modern-day film noir finds cynical hit man Mick (Anthony LaPaglia) tiring of his job and asking his boss, mob kingpin George (Peter Boyle), for time off. George gives him the assignment of his life, however, prompting Mick's soul-searching to reach new heights. Mick is asked to kill the sultry Fiona (Mimi Rogers), who owes George money and claims she wants to die. But as Mick spends time with her, he finds himself falling for her.",
            "backdrop": "movie_images/backdrop/502.png",
            "poster": "movie_images/poster/502.png",
            "video": 0
        },
        "503": {
            "id": "503",
            "title": "Welcome to the Dollhouse",
            "overview": "An unattractive 7th grader struggles to cope with suburban life as the middle child with un-attentive parents and bullies at school.",
            "backdrop": "movie_images/backdrop/503.png",
            "poster": "movie_images/poster/503.png",
            "video": 0
        },
        "504": {
            "id": "504",
            "title": "Germinal",
            "overview": "It's mid 19th century, north of France. The story of a coal miner's town. They are exploited by the mine's owner. One day the decide to go on strike, and then the authorities repress them",
            "backdrop": "movie_images/backdrop/504.png",
            "poster": "movie_images/poster/504.png",
            "video": 0
        },
        "4342": {
            "id": "4342",
            "title": "Raggedy Man",
            "overview": "Nita, a divorced mother of two boys, is stuck working as a telephone operator in a small Texas town in World War II. Her friendship with a sailor on leave causes tongues to wag in town.",
            "backdrop": "movie_images/backdrop/4342.png",
            "poster": "movie_images/poster/4342.png",
            "video": 0
        },
        "506": {
            "id": "506",
            "title": "Cronos",
            "overview": "Faced with his own mortality, an ingenious alchemist tried to perfect an invention that would provide him with the key to eternal life. It was called the Cronos device. When he died more than 400 years later, he took the secrets of this remarkable device to the grave with him. Now, an elderly antiques dealer has found the hellish machine hidden in a statue and learns about its incredible powers. The more he uses the device, the younger he becomes...but nothing comes without a price. Life after death is just the beginning as this nerve-shattering thriller unfolds and the fountain of youth turns bloody.",
            "backdrop": "movie_images/backdrop/506.png",
            "poster": "movie_images/poster/506.png",
            "video": 0
        },
        "507": {
            "id": "507",
            "title": "Kika",
            "overview": "Kika, a young cosmetologist, is called to the mansion of Nicolas, an American writer to make-up the corpse of his stepson, Ramon. Ramon, who is not dead, is revived by Kika's attentions and she then moves in with him. They might live happily ever after but first they have to cope with Kika's affair with Nicolas, the suspicious death of Ramon's mother and the intrusive gaze of tabloid-TV star and Ramon's ex-psychologist Andrea Scarface.",
            "backdrop": "movie_images/backdrop/507.png",
            "poster": "movie_images/poster/507.png",
            "video": 0
        },
        "508": {
            "id": "508",
            "title": "Bhaji on the Beach",
            "overview": "A group of women of Indian descent take a trip together from their home in Birmingham, England to the beach resort of Blackpool.",
            "backdrop": "movie_images/backdrop/508.png",
            "poster": "movie_images/poster/508.png",
            "video": 0
        },
        "253": {
            "id": "253",
            "title": "Nobody's Fool",
            "overview": "Sully is a rascally ne'er-do-well approaching retirement age. While he is pressing a worker's compensation suit for a bad knee, he secretly works for his nemesis, Carl, and flirts with Carl's young wife Toby. Sully's long- forgotten son and family have moved back to town, so Sully faces unfamiliar family responsibilities. Meanwhile, Sully's landlady's banker son plots to push through a new development and evict Sully from his mother's life.",
            "backdrop": "movie_images/backdrop/253.png",
            "poster": "movie_images/poster/253.png",
            "video": 0
        },
        "4094": {
            "id": "4094",
            "title": "The New Guy",
            "overview": "Nerdy high school senior Dizzy Harrison has finally gotten lucky -- after purposely getting expelled, he takes lessons in 'badass cool' from a convict and enrolls at a new school. But can he keep up the ruse?",
            "backdrop": "movie_images/backdrop/4094.png",
            "poster": "movie_images/poster/4094.png",
            "video": 0
        },
        "255": {
            "id": "255",
            "title": "New Jersey Drive",
            "overview": "New Jersey Drive is a 1995 film about black youths in Newark, New Jersey, the unofficial \"car theft capital of the world\". Their favorite pastime is that of everybody in their neighborhood: stealing cars and joyriding. The trouble starts when they steal a police car and the cops launch a violent offensive that involves beating and even shooting suspects.",
            "backdrop": "movie_images/backdrop/255.png",
            "poster": "movie_images/poster/255.png",
            "video": 0
        }
    }
}

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html')

def first_page(request):
    return render(request, 'personal/first.html', {'content':data})

def square(request):
    if request.method == 'POST':
        no = int(request.POST['number'])**2
        response = {}
        response['answer'] = no

        return HttpResponse(no)
    else:
        return HttpResponse('problem')

"""
ASGI config for nutshell project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nutshell.settings')

application = get_asgi_application()

'''
To clarify things going in yes Joe is an object :)

Joe-K: The Origin Story ->

Scene 1
Rafiki: We would like to take a few moments to get you acquainted with the story of Joe.
Tiki: Joe was born just a few moments ago to {Joe.parents}. Of course, {Joe.dad | Joe.mom} is the king
of Pride Rock. All the animals are gathering to welcome Joe into the world.
Rafiki & Tiki: And now, it is time.
Lion Roar – animals gather around Pride Rock
THE CIRCLE OF LIFE
(Sunrise on African grassland)
African Singers: From the day we arrive on the planet
 And blinking, step into the sun
 There's more to see than can ever be seen
 More to do than can ever be done
 There's far too much to take in here
 More to find than can ever be found
But the sun rolling high
In the sapphire sky
 Keeps great and small on the endless round
({Joe.parent_who_won} on Pride Rock)
All: It's the Circle of Life
And it moves us all 
{Zazu bows to {Joe.parent_hash_tag_won}, who smiles and nods at him}
Through despair and hope
Through faith and love
{Rafiki & Tiki, pass between animals – who part and bow – walks to Pride Rock to where {Joe.parent_that_did_nothing} is
standing.}
Till we find our place
On the path unwinding
{Rafiki & Tiki and {Joe.non_birther} greet.}
In the Circle
The Circle of Life
{{Joe.lazy_bones} leads Rafiki & Tiki over to {Joe.champion} who is holding Simba}
{Rafiki puts the juice and sand he collects on Joe's brow-- A ceremonial crown. He then picks
Joe up and ascends to the point of Pride Rock. {Joe.lame} and {Joe.chief} follow. With a crescendo in
the music and a restatement of the refrain, Rafiki holds Joe up for the crowd to view.
All: It’s The Circle of life
 And it moves us all
Through despair and hope
Through faith and love
Till we find our place
In the path unwinding
In the Circle
The Circle of life 


LOL, hope this made you laugh :)
If you are confused/ laughing I did my job lol.

Real script here-> http://frimley.surrey.sch.uk/wp-content/uploads/2018/05/lion-king-script-word.pdf
'''
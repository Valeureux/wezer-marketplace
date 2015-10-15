# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Yannick Buron and Valeureux
#    Copyright 2013 Yannick Buron and Valeureux
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Marketplace Crowdfunding',
    'version': '1.0',
    'category': 'Community',
    'depends': [
        'crowdfunding',
        'marketplace'
    ],
    'author': 'Yannick Buron and Valeureux',
    'license': 'AGPL-3',
    'website': 'https://launchpad.net/marketplace',
    'description': """
Marketplace Crowdfunding
=================

""",
    'demo': [],
    'data': ['marketplace_crowdfunding_view.xml'],
    'installable': True,
    'application': True,
}

{
    'name': 'Calyx Test AgusCFx',
    'version': '15.0.1.0.0',
    'description': '',
    'author': 'AgusCFx',
    'website': 'https://github.com/AgusCFx',
    'license': 'LGPL-3',
    'category': '',
    'depends': [
        'sale_management','stock','account','sale_stock'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/channel_secuence.xml',
        'views/sales_channels.xml',
        'views/credit_groups.xml',
        'views/sales_view.xml'
    ],
    'auto_install': False,
    'application': False,
}
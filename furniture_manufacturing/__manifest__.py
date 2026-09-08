{
    'name': 'Furniture Manufacturing',
    'version': '1.0',
    'summary': 'Custom module for Furniture Manufacturing Company',
    'description': """
        Handles technical requirements for the Furniture Manufacturing workflow:
        - Website Order boolean on Sales Orders
        - Material Brands configuration for Products and Purchase Orders
    """,
    'category': 'Customizations',
    'author': 'Your Name',
    'depends': ['sale_management', 'purchase', 'website_sale', 'stock', 'mrp'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/product_brand_views.xml',
        'views/product_template_views.xml',
        'views/purchase_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}

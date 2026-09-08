# Odoo Technical & Functional Tasks

A collection of custom Odoo modules and practical tasks covering **Technical Customizations**, **Functional Workflows**, **ORM Modeling**, and **Cross-Module Integration**.

---

## 📚 Repository Modules Overview

| Module Name | Type | Key Odoo Apps / Dependencies | Description |
| :--- | :--- | :--- | :--- |
| 🪑 **`furniture_manufacturing`** | Functional & Technical | `sale_management`, `purchase`, `website_sale`, `stock`, `mrp` | Custom workflow for Furniture Manufacturing: Material Brand configuration across Products & Purchase Orders, and Website Sale order customization. |
| 🏡 **`estate`** | Technical Core | `base` | Real Estate property management module featuring property types, tags, offers, computed fields, onchange handlers, and custom XML views. |
| 🧾 **`estate_accounts`** | Cross-Module Integration | `estate`, `account` | Automatic accounting and invoicing integration extending Real Estate property sale actions. |

---

## ⚙️ Detailed Module Features

### 1. Furniture Manufacturing (`furniture_manufacturing`)
- **Functional Requirements**:
  - Track **Material Brands** on Product Templates and Purchase Order lines.
  - Automatically flag Sales Orders coming from the Website that require custom furniture manufacturing.
  - Full traceability across Purchasing, Inventory, MRP (Manufacturing), and Sales.
- **Technical Implementation**:
  - **Models**: `product.brand`, `product.template`, `sale.order`, `purchase.order.line`.
  - **Views**: Form & Tree extensions for `sale.order`, `purchase.order`, `product.template`, and new brand management views.
  - **Security**: Access rights configured in `ir.model.access.csv`.

### 2. Real Estate Management (`estate`)
- **Functional Requirements**:
  - Property listings lifecycle management (New → Offer Received → Offer Accepted → Sold / Canceled).
  - Offers tracking with buyer details, validity date calculations, and offer acceptance/refusal actions.
- **Technical Implementation**:
  - **Models**: `estate.property`, `estate.property.offer`, `estate.property.tag`, `estate.property.type`, `res.users` inheritance.
  - **Features**: `@api.depends` for computed fields (`total_area`, `best_price`), `@api.onchange` handlers, SQL constraints, and Python validation rules.
  - **Views**: Form views with statusbars, notebook pages, inline offer lists, Tree/List views, Search filters, and Kanban views.

### 3. Estate Accounting (`estate_accounts`)
- **Functional Requirements**:
  - Automatically create customer invoices (`account.move`) when a property is marked as **Sold**.
  - Adds commission percentage and administrative fee lines to generated invoices.
- **Technical Implementation**:
  - Extends `estate.property` action buttons via object inheritance (`super()`).
  - Interacts with Odoo's core `account.move` and `account.move.line` models.

---

## 🛠️ Tech Stack & Requirements

- **Framework**: Odoo (v16 / v17)
- **Language**: Python 3.x, XML, CSV
- **Database**: PostgreSQL

---

## 🚀 Getting Started

1. Clone this repository into your Odoo custom addons path:
   ```bash
   git clone https://github.com/AbdelrahmanAyman208/odoo-technical-functional-tasks.git
   ```
2. Add the repository directory to your `odoo.conf` file under `addons_path`:
   ```ini
   addons_path = /path/to/odoo/addons,/path/to/odoo-technical-functional-tasks
   ```
3. Restart your Odoo server and update the App List in Developer Mode.
4. Install `furniture_manufacturing` or `estate` from the Apps menu.

---

## 📜 License
This project is open-source and available under the [LGPL-3.0 License](LICENSE).

# Relational Schema Mapping: Global Logistics Inc.

**Assignment:** Relational Schema Mapping
**Scenario:** Global Logistics Inc. Fleet and Shipment Database

---

## 1. Introduction

Global Logistics Inc. runs a fleet of delivery vehicles. It needs a database to track four things: its warehouses, its delivery drivers, its vehicles, and the shipments those drivers and vehicles carry. The business requirements were written in plain language. This paper turns them into a formal relational schema. For each table it gives the attributes, the primary key (PK), the foreign keys (FK), and the rules that link the tables.

The work follows four steps:

1. Identify the entities and their attributes in the requirements.
2. Identify the relationships between the entities and their cardinality.
3. Map the entities and relationships to relations (tables), placing primary and foreign keys.
4. Check the result against the normal forms (1NF, 2NF, 3NF).

---

## 2. Step 1: Identify Entities and Attributes

Each noun group in the requirements that has its own identifier becomes an entity.

| Entity | Identifier in the requirements | Attributes stated in the requirements |
|---|---|---|
| Warehouse | Location ID | Location ID, capacity, manager name |
| Delivery Driver | Driver ID | Driver ID, name, license class |
| Vehicle | VIN | VIN, make, model, maintenance status |
| Shipment | Tracking Number | Tracking Number, weight, destination, assigned driver, assigned vehicle |

Two attributes of Shipment, "assigned driver" and "assigned vehicle," are not plain data values. They point to rows in other entities. They are relationships, so they become foreign keys in Step 3.

---

## 3. Step 2: Identify Relationships and Cardinality

| Relationship | Entities | Cardinality | Participation | Basis |
|---|---|---|---|---|
| **is assigned to** | Driver to Shipment | 1 : N | A shipment has exactly one assigned driver. A driver may have zero or many shipments. | Stated: "assigned driver" |
| **carries** | Vehicle to Shipment | 1 : N | A shipment has exactly one assigned vehicle. A vehicle may carry zero or many shipments. | Stated: "assigned vehicle" |
| **ships from** | Warehouse to Shipment | 1 : N | A shipment leaves from exactly one warehouse. A warehouse may send out zero or many shipments. | Assumption (see Section 6) |

**Why 1 : N and not M : N?** Each shipment has one tracking number and is assigned one driver and one vehicle. Over time a driver handles many shipments, and so does a vehicle. So the "many" side is always Shipment. In a 1 : N relationship, the foreign key goes on the "many" side. No junction table is needed.

---

## 4. Step 3: The Formal Relational Schema

### 4.1 Schema in standard notation

Primary keys are <u>underlined</u>. Foreign keys are marked with an asterisk (\*) and show the table they refer to.

> **WAREHOUSE** (<u>LocationID</u>, Capacity, ManagerName)
>
> **DRIVER** (<u>DriverID</u>, FirstName, LastName, LicenseClass)
>
> **VEHICLE** (<u>VIN</u>, Make, Model, MaintenanceStatus)
>
> **SHIPMENT** (<u>TrackingNumber</u>, Weight, DestStreet, DestCity, DestState, DestPostalCode, DestCountry, DriverID\*, VIN\*, OriginLocationID\*)
>
> &nbsp;&nbsp;&nbsp;&nbsp;SHIPMENT.DriverID → DRIVER.DriverID
> &nbsp;&nbsp;&nbsp;&nbsp;SHIPMENT.VIN → VEHICLE.VIN
> &nbsp;&nbsp;&nbsp;&nbsp;SHIPMENT.OriginLocationID → WAREHOUSE.LocationID

### 4.2 Table definitions

#### WAREHOUSE

| Attribute | Data Type | Key | Constraints | Description |
|---|---|---|---|---|
| LocationID | VARCHAR(10) | **PK** | NOT NULL, UNIQUE | Unique code for each warehouse location |
| Capacity | INT | | NOT NULL, CHECK (Capacity > 0) | Storage capacity (for example, in pallets or cubic meters) |
| ManagerName | VARCHAR(100) | | NOT NULL | Name of the warehouse manager |

#### DRIVER

| Attribute | Data Type | Key | Constraints | Description |
|---|---|---|---|---|
| DriverID | VARCHAR(10) | **PK** | NOT NULL, UNIQUE | Unique employee ID for the driver |
| FirstName | VARCHAR(50) | | NOT NULL | Driver's first name |
| LastName | VARCHAR(50) | | NOT NULL | Driver's last name |
| LicenseClass | CHAR(1) | | NOT NULL, CHECK (LicenseClass IN ('A','B','C')) | Commercial driver's license class |

#### VEHICLE

| Attribute | Data Type | Key | Constraints | Description |
|---|---|---|---|---|
| VIN | CHAR(17) | **PK** | NOT NULL, UNIQUE | 17-character Vehicle Identification Number |
| Make | VARCHAR(30) | | NOT NULL | Manufacturer (for example, Ford, Freightliner) |
| Model | VARCHAR(30) | | NOT NULL | Vehicle model |
| MaintenanceStatus | VARCHAR(20) | | NOT NULL, DEFAULT 'Active', CHECK (MaintenanceStatus IN ('Active','In Maintenance','Out of Service')) | Current service condition |

#### SHIPMENT

| Attribute | Data Type | Key | Constraints | Description |
|---|---|---|---|---|
| TrackingNumber | VARCHAR(20) | **PK** | NOT NULL, UNIQUE | Unique tracking number for the shipment |
| Weight | DECIMAL(10,2) | | NOT NULL, CHECK (Weight > 0) | Shipment weight (kg) |
| DestStreet | VARCHAR(100) | | NOT NULL | Destination street address |
| DestCity | VARCHAR(50) | | NOT NULL | Destination city |
| DestState | VARCHAR(50) | | | Destination state or province |
| DestPostalCode | VARCHAR(15) | | | Destination postal code |
| DestCountry | VARCHAR(50) | | NOT NULL | Destination country |
| DriverID | VARCHAR(10) | **FK** | NOT NULL, REFERENCES DRIVER(DriverID) | The assigned driver |
| VIN | CHAR(17) | **FK** | NOT NULL, REFERENCES VEHICLE(VIN) | The assigned vehicle |
| OriginLocationID | VARCHAR(10) | **FK** | NOT NULL, REFERENCES WAREHOUSE(LocationID) | The warehouse the shipment leaves from |

### 4.3 Primary and foreign key summary

| Table | Primary Key | Foreign Key(s) | References | On Delete | On Update |
|---|---|---|---|---|---|
| WAREHOUSE | LocationID | none | none | n/a | n/a |
| DRIVER | DriverID | none | none | n/a | n/a |
| VEHICLE | VIN | none | none | n/a | n/a |
| SHIPMENT | TrackingNumber | DriverID | DRIVER(DriverID) | RESTRICT | CASCADE |
| | | VIN | VEHICLE(VIN) | RESTRICT | CASCADE |
| | | OriginLocationID | WAREHOUSE(LocationID) | RESTRICT | CASCADE |

**Why RESTRICT on delete?** A shipment is a business record. It may be needed for billing, audits, or customer questions. If a driver, vehicle, or warehouse still has shipments, the database blocks its deletion. This stops "orphan" shipments that point to nothing. **Why CASCADE on update?** If a key value is ever corrected (for example, a mistyped Location ID), the change carries through to every shipment that uses it.

### 4.4 Entity-Relationship diagram (crow's-foot, text form)

```
 +----------------+          +----------------+          +----------------+
 |   WAREHOUSE    |          |     DRIVER     |          |    VEHICLE     |
 |----------------|          |----------------|          |----------------|
 | PK LocationID  |          | PK DriverID    |          | PK VIN         |
 |    Capacity    |          |    FirstName   |          |    Make        |
 |    ManagerName |          |    LastName    |          |    Model       |
 +-------+--------+          |    LicenseClass|          |    MaintStatus |
         |                   +-------+--------+          +-------+--------+
         | 1                         | 1                         | 1
         | ships from                | is assigned to            | carries
         |                           |                           |
         | 0..N                      | 0..N                      | 0..N
         +-------------------+       |       +-------------------+
                             |       |       |
                     +-------v-------v-------v-------+
                     |           SHIPMENT            |
                     |-------------------------------|
                     | PK TrackingNumber             |
                     |    Weight                     |
                     |    DestStreet, DestCity,      |
                     |    DestState, DestPostalCode, |
                     |    DestCountry                |
                     | FK OriginLocationID -> WAREHOUSE
                     | FK DriverID         -> DRIVER |
                     | FK VIN              -> VEHICLE|
                     +-------------------------------+
```

---

## 5. Step 4: Normalization Check

**First Normal Form (1NF): every value is atomic, and there are no repeating groups.**
The requirements list "name" for drivers and "destination" for shipments. Each of these holds more than one piece of data. "Name" is split into FirstName and LastName. "Destination" is split into street, city, state, postal code, and country. After this, every column holds one value, and every table has a primary key. The schema is in 1NF.

**Second Normal Form (2NF): no partial dependency on part of a composite key.**
Every table has a single-column primary key. A partial dependency can only happen with a composite key, so every table is in 2NF automatically.

**Third Normal Form (3NF): no transitive dependency (a non-key column depending on another non-key column).**
- In SHIPMENT, the driver's name and license class are *not* stored. Only DriverID is stored, and the other details are found by joining to DRIVER. If DriverName were kept in SHIPMENT, it would depend on DriverID, not on TrackingNumber. That is a transitive dependency. The same reasoning keeps Make, Model, and MaintenanceStatus out of SHIPMENT and inside VEHICLE.
- In WAREHOUSE, Capacity and ManagerName both depend only on LocationID.
- In VEHICLE, Make and Model both depend on VIN. In this scope they do not depend on each other.

The schema is in **3NF**. Each fact is stored in one place, which prevents update, insert, and delete anomalies.

---

## 6. Assumptions and Design Decisions

1. **Origin warehouse on Shipment.** The requirements list Warehouses but do not say how they link to other entities. A shipment that is delivered must leave from somewhere, so SHIPMENT has an `OriginLocationID` foreign key. This makes Warehouse part of the model instead of an unconnected table. If the business does not need this, the column can be dropped without affecting the rest of the schema.
2. **One driver and one vehicle per shipment.** The requirements say "assigned driver" and "assigned vehicle" in the singular, so each is a single, required (NOT NULL) foreign key. If a shipment could move between several drivers or vehicles (for example, relay legs), a `SHIPMENT_LEG` junction table would be needed.
3. **Manager name stays an attribute.** The requirements give only a manager *name*, with no ID or other details. So it is stored as a column of WAREHOUSE. If the company later tracks managers as employees, ManagerName would be replaced by a `ManagerID` foreign key to an EMPLOYEE table.
4. **Natural keys are used.** Location ID, Driver ID, VIN, and Tracking Number are already unique business identifiers. They serve as primary keys, so no surrogate (auto-number) keys are added.
5. **Controlled values.** LicenseClass and MaintenanceStatus are limited to fixed lists using CHECK constraints. This keeps the data consistent.

---

## 7. SQL Implementation (DDL)

The script below builds the schema in standard SQL. Tables are created in dependency order: parent tables before SHIPMENT.

```sql
CREATE TABLE WAREHOUSE (
    LocationID   VARCHAR(10)  NOT NULL,
    Capacity     INT          NOT NULL CHECK (Capacity > 0),
    ManagerName  VARCHAR(100) NOT NULL,
    CONSTRAINT PK_Warehouse PRIMARY KEY (LocationID)
);

CREATE TABLE DRIVER (
    DriverID      VARCHAR(10) NOT NULL,
    FirstName     VARCHAR(50) NOT NULL,
    LastName      VARCHAR(50) NOT NULL,
    LicenseClass  CHAR(1)     NOT NULL CHECK (LicenseClass IN ('A', 'B', 'C')),
    CONSTRAINT PK_Driver PRIMARY KEY (DriverID)
);

CREATE TABLE VEHICLE (
    VIN                CHAR(17)    NOT NULL,
    Make               VARCHAR(30) NOT NULL,
    Model              VARCHAR(30) NOT NULL,
    MaintenanceStatus  VARCHAR(20) NOT NULL DEFAULT 'Active'
        CHECK (MaintenanceStatus IN ('Active', 'In Maintenance', 'Out of Service')),
    CONSTRAINT PK_Vehicle PRIMARY KEY (VIN)
);

CREATE TABLE SHIPMENT (
    TrackingNumber    VARCHAR(20)   NOT NULL,
    Weight            DECIMAL(10,2) NOT NULL CHECK (Weight > 0),
    DestStreet        VARCHAR(100)  NOT NULL,
    DestCity          VARCHAR(50)   NOT NULL,
    DestState         VARCHAR(50),
    DestPostalCode    VARCHAR(15),
    DestCountry       VARCHAR(50)   NOT NULL,
    DriverID          VARCHAR(10)   NOT NULL,
    VIN               CHAR(17)      NOT NULL,
    OriginLocationID  VARCHAR(10)   NOT NULL,
    CONSTRAINT PK_Shipment PRIMARY KEY (TrackingNumber),
    CONSTRAINT FK_Shipment_Driver FOREIGN KEY (DriverID)
        REFERENCES DRIVER (DriverID)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT FK_Shipment_Vehicle FOREIGN KEY (VIN)
        REFERENCES VEHICLE (VIN)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT FK_Shipment_Warehouse FOREIGN KEY (OriginLocationID)
        REFERENCES WAREHOUSE (LocationID)
        ON DELETE RESTRICT ON UPDATE CASCADE
);
```

### 7.1 Sample data and a test of the keys

```sql
INSERT INTO WAREHOUSE VALUES ('LAX01', 5000, 'Maria Lopez');
INSERT INTO DRIVER    VALUES ('D1001', 'James', 'Carter', 'A');
INSERT INTO VEHICLE   VALUES ('1FTFW1E50NFA00001', 'Ford', 'Transit', 'Active');

INSERT INTO SHIPMENT VALUES
  ('GLI-000123', 245.50, '1200 Market St', 'San Francisco', 'CA', '94102', 'USA',
   'D1001', '1FTFW1E50NFA00001', 'LAX01');

-- Rejected: driver D9999 does not exist (foreign key violation)
INSERT INTO SHIPMENT VALUES
  ('GLI-000124', 80.00, '5 Main St', 'Reno', 'NV', '89501', 'USA',
   'D9999', '1FTFW1E50NFA00001', 'LAX01');

-- Rejected: driver D1001 still has shipments (ON DELETE RESTRICT)
DELETE FROM DRIVER WHERE DriverID = 'D1001';
```

### 7.2 Example query using the relationships

The query below lists each shipment with its driver, vehicle, and origin warehouse. It shows how the foreign keys link the four tables.

```sql
SELECT  s.TrackingNumber,
        s.Weight,
        s.DestCity,
        d.FirstName || ' ' || d.LastName AS DriverName,
        d.LicenseClass,
        v.Make, v.Model, v.MaintenanceStatus,
        w.LocationID AS OriginWarehouse,
        w.ManagerName
FROM    SHIPMENT  s
JOIN    DRIVER    d ON s.DriverID         = d.DriverID
JOIN    VEHICLE   v ON s.VIN              = v.VIN
JOIN    WAREHOUSE w ON s.OriginLocationID = w.LocationID;
```

---

## 8. Conclusion

The requirements for Global Logistics Inc. map to four relations: WAREHOUSE, DRIVER, VEHICLE, and SHIPMENT. The first three are independent parent tables, each with a natural primary key (LocationID, DriverID, VIN). SHIPMENT, keyed by TrackingNumber, is the central child table. Its three foreign keys, DriverID, VIN, and OriginLocationID, turn the stated "assigned driver" and "assigned vehicle" requirements, plus the originating warehouse, into enforced one-to-many relationships. The schema is in Third Normal Form. Referential integrity rules keep shipment records from pointing to drivers, vehicles, or warehouses that do not exist.

---

## References

Connolly, T., & Begg, C. (2015). *Database systems: A practical approach to design, implementation, and management* (6th ed.). Pearson.

Codd, E. F. (1970). A relational model of data for large shared data banks. *Communications of the ACM, 13*(6), 377–387. https://doi.org/10.1145/362384.362685

Elmasri, R., & Navathe, S. B. (2016). *Fundamentals of database systems* (7th ed.). Pearson.

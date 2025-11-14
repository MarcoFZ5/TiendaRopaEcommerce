USE master
GO

CREATE DATABASE DB_TiendaRopa
GO

USE DB_TiendaRopa 
GO

CREATE SCHEMA SC_TiendaRopa
GO

-- Tabla Categoria
CREATE TABLE SC_TiendaRopa.T_Categoria (
    id_categoria INT IDENTITY(1,1) PRIMARY KEY,
    nombre       VARCHAR(100) NOT NULL,
    descripcion  VARCHAR(MAX) NULL
)
GO

-- Tabla Producto
CREATE TABLE SC_TiendaRopa.T_Producto (
    id_producto  INT IDENTITY(1,1) PRIMARY KEY,
    nombre       VARCHAR(150)   NOT NULL,
    descripcion  VARCHAR(MAX)   NULL,
    id_categoria INT            NOT NULL,

    CONSTRAINT FK_Producto_T_Categoria
        FOREIGN KEY (id_categoria) REFERENCES SC_TiendaRopa.T_Categoria(id_categoria)
)
GO

-- Tabla Producto Variacion

CREATE TABLE SC_TiendaRopa.T_ProductoVariacion (
    id_variacion INT IDENTITY(1,1) PRIMARY KEY,
    id_producto  INT NOT NULL,
    talla        VARCHAR(50) NOT NULL,
    stock        INT NOT NULL DEFAULT 0,
    precio       DECIMAL(10,2) NOT NULL,

    CONSTRAINT FK_ProdVar_Producto
        FOREIGN KEY (id_producto)
        REFERENCES SC_TiendaRopa.T_Producto(id_producto)
)
GO


-- Tabla Carrito
CREATE TABLE SC_TiendaRopa.T_Carrito (
    id_carrito     INT IDENTITY(1,1) PRIMARY KEY,
    fecha_creacion DATETIME      NOT NULL DEFAULT GETDATE(),
    total          DECIMAL(10,2) NOT NULL DEFAULT 0,
    estado         VARCHAR(30)   NOT NULL CHECK (estado IN ('CREADO', 'PENDIENTE', 'PAGADO')) DEFAULT 'CREADO',
    metodo_pago    VARCHAR(50)   NOT NULL
)
GO

-- Tabla ProductoCarrito

CREATE TABLE SC_TiendaRopa.T_ProductoCarrito (
    id_producto_carrito INT IDENTITY(1,1) PRIMARY KEY,
    id_carrito          INT NOT NULL,
    id_variacion        INT NOT NULL,
    cantidad            INT NOT NULL DEFAULT 1,
    subtotal            DECIMAL(10,2) NOT NULL,

    CONSTRAINT FK_ProdCarrito_Carrito
        FOREIGN KEY (id_carrito)
        REFERENCES SC_TiendaRopa.T_Carrito(id_carrito),

    CONSTRAINT FK_ProdCarrito_ProdVar
        FOREIGN KEY (id_variacion)
        REFERENCES SC_TiendaRopa.T_ProductoVariacion(id_variacion),

    CONSTRAINT UQ_ProdCarrito UNIQUE (id_carrito, id_variacion),

    -- Validaciones
    CONSTRAINT CK_ProdCarrito_Cantidad CHECK (cantidad > 0),
    CONSTRAINT CK_ProdCarrito_Subtotal CHECK (subtotal >= 0)
)
GO

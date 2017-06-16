USE [COSHI]
GO

/****** Object:  Table [dbo].[computerAudited]    Script Date: 6/16/2017 12:54:35 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[computerAudited](
	[computerID] [int] IDENTITY(1,1) NOT NULL,
	[assetTag] [nvarchar](20) NULL,
	[pcLifeCyle] [bit] NULL,
	[fixedAsset] [bit] NULL,
	[computerName] [nvarchar](100) NULL,
	[computerOwner] [nvarchar](100) NULL,
	[computerCurator] [nvarchar](100) NULL,
	[computerLocation] [nvarchar](100) NULL,
	[HW_Make] [nvarchar](100) NULL,
	[HW_Model] [nvarchar](100) NULL,
	[HW_Type] [nvarchar](100) NULL,
	[serialNumber] [nvarchar](100) NULL,
	[vendor] [nvarchar](100) NULL,
	[vendorSerialNumber] [nvarchar](100) NULL,
	[purchaseOrder] [nvarchar](100) NULL,
	[purchaseFundedBy] [nvarchar](100) NULL,
	[purchaseAmount] [nvarchar](100) NULL,
	[purchaseDate] [date] NULL,
	[organizationNumber] [nvarchar](100) NULL,
	[department] [nvarchar](100) NULL,
	[OS] [nvarchar](100) NULL,
	[OS_Build] [nvarchar](100) NULL,
	[OS_SP] [nvarchar](100) NULL,
	[CPU] [nvarchar](max) NULL,
	[mainHDD] [nvarchar](max) NULL,
	[RAM_Total] [nvarchar](100) NULL,
	[macAddress] [nvarchar](max) NULL,
	[BIOS_Manufacturer] [nvarchar](100) NULL,
	[BIOS_Name] [nvarchar](100) NULL,
	[BIOS_Version] [nvarchar](100) NULL,
	[domain] [nvarchar](50) NULL,
	[ouPath] [nvarchar](max) NULL,
	[upTime] [datetime] NULL,
	[lastLoginUser] [nvarchar](100) NULL,
	[lastLoginDate] [date] NULL,
	[dateAdded] [date] NULL,
	[dateModified] [date] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO
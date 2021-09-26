# coding: utf-8
from sqlalchemy import BigInteger, Boolean, Column, DECIMAL, DateTime, ForeignKey, Integer, String, Table, Time, Unicode, text
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class BinaryState(Base):
    __tablename__ = 'BinaryStates'

    Id = Column(Integer, primary_key=True)
    On = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    Off = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    CompanyId = Column(Integer)
    CreatedBy = Column(UNIQUEIDENTIFIER)
    DateCreated = Column(DateTime)
    DateModified = Column(DateTime)
    LastModifiedBy = Column(UNIQUEIDENTIFIER)


class Branch(Base):
    __tablename__ = 'Branch'

    BranchID = Column(Integer, primary_key=True)
    BranchCity = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    BranchAddress = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    BranchState = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    BranchZipcode = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    BranchCountry = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    CompanyID = Column(Integer, nullable=False)
    LastModifiedBy = Column(Integer, nullable=False)
    DateModified = Column(DateTime, nullable=False)
    DateCreated = Column(DateTime, nullable=False)
    CreatedBy = Column(UNIQUEIDENTIFIER)


class BreakDown(Base):
    __tablename__ = 'BreakDown'

    Id = Column(Integer, primary_key=True)
    BreakdownName = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    IsActive = Column(Boolean, server_default=text("((0))"))
    CreatedBy = Column(UNIQUEIDENTIFIER)
    DateCreated = Column(DateTime)
    DateModified = Column(DateTime)
    LastModifiedBy = Column(UNIQUEIDENTIFIER)


class BreakDownDetail(Base):
    __tablename__ = 'BreakDownDetails'

    Id = Column(Integer, primary_key=True)
    BreakDownId = Column(Integer)
    PerRecord = Column(DECIMAL(18, 8), server_default=text("((0))"))
    PerSms = Column(DECIMAL(18, 8), server_default=text("((0))"))
    PerCall = Column(DECIMAL(18, 8), server_default=text("((0))"))
    NoOfRecordsLimit = Column(Integer, server_default=text("((0))"))
    CreatedBy = Column(UNIQUEIDENTIFIER)
    DateCreated = Column(DateTime)
    DateModified = Column(DateTime)
    LastModifiedBy = Column(UNIQUEIDENTIFIER)


class CallHistory(Base):
    __tablename__ = 'CallHistory'

    Id = Column(Integer, primary_key=True)
    UserId = Column(UNIQUEIDENTIFIER)
    CompanyId = Column(Integer)
    Description = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'), server_default=text("('')"))
    CreatedBy = Column(UNIQUEIDENTIFIER)
    DateCreated = Column(DateTime)
    DateModified = Column(DateTime)
    LastModifiedBy = Column(UNIQUEIDENTIFIER)


class CollaboratorAccessRole(Base):
    __tablename__ = 'CollaboratorAccessRoles'

    Id = Column(Integer, primary_key=True)
    CompanyId = Column(Integer, nullable=False)
    RoleId = Column(UNIQUEIDENTIFIER, nullable=False)
    DateCreated = Column(DateTime, nullable=False)
    CreatedBy = Column(UNIQUEIDENTIFIER, nullable=False)
    DateModified = Column(DateTime, nullable=False)
    LastModifiedBy = Column(UNIQUEIDENTIFIER, nullable=False)


class Company(Base):
    __tablename__ = 'Company'

    CompanyID = Column(Integer, primary_key=True)
    CompanyName = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CompanyAddress = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    CompanyCity = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    CompanyState = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    CompanyZipCode = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    PlanID = Column(Integer)
    IndustryId = Column(Integer)
    CompanyStripeId = Column(String(500, 'SQL_Latin1_General_CP1_CI_AS'))
    DateCreated = Column(DateTime, nullable=False)
    CompanyBlobUrl = Column(Unicode)
    CompanyCountry = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    DateModified = Column(DateTime)
    LastModifiedBy = Column(Integer)
    IsPermitNewUsersSameDomain = Column(Boolean, nullable=False, server_default=text("((0))"))
    CreatedBy = Column(UNIQUEIDENTIFIER)
    NoOfRecordsUsed = Column(Integer, server_default=text("((0))"))
    FeatureId = Column(Integer)
    BreakDownId = Column(Integer)
    IsFixed = Column(Boolean, nullable=False, server_default=text("((0))"))
    FixedPrice = Column(DECIMAL(18, 2), server_default=text("((0.00))"))
    BillingStartDate = Column(DateTime)
    BillingEndDate = Column(DateTime)


class CriticalityType(Base):
    __tablename__ = 'CriticalityTypes'

    Id = Column(Integer, primary_key=True)
    TypeName = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)


class CustomNotificationSetting(Base):
    __tablename__ = 'CustomNotificationSetting'

    CustomNotificationSettingId = Column(Integer, primary_key=True)
    UserId = Column(UNIQUEIDENTIFIER, nullable=False)
    IsSMS = Column(Boolean, nullable=False)
    IsCall = Column(Boolean, nullable=False)
    IsEmail = Column(Boolean, nullable=False)
    DateCreated = Column(DateTime, nullable=False)
    NotificationTypeId = Column(Integer)


class CustomReport(Base):
    __tablename__ = 'CustomReports'

    CustomReportId = Column(Integer, primary_key=True)
    Description = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'))
    CreatedBy = Column(UNIQUEIDENTIFIER)
    DateCreated = Column(DateTime)
    LastModifiedBy = Column(UNIQUEIDENTIFIER)
    DateModified = Column(DateTime)
    ReportId = Column(Integer)


class DBChangeLog(Base):
    __tablename__ = 'DBChangeLog'

    DBChangeLogID = Column(Integer, primary_key=True)
    DatabaseName = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    EventType = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    ObjectName = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    ObjectType = Column(String(25, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    SqlCommand = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    EventDate = Column(DateTime, nullable=False)
    LoginName = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)


class DataType(Base):
    __tablename__ = 'DataType'

    DataTypeID = Column(Integer, primary_key=True)
    DataTypeName = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    LastModifiedBy = Column(Integer)
    DateCreated = Column(DateTime)
    DateModified = Column(DateTime)
    CreatedBy = Column(UNIQUEIDENTIFIER)


class DaysOff(Base):
    __tablename__ = 'DaysOff'

    DayID = Column(Integer, primary_key=True)
    SensorID = Column(String(150, 'SQL_Latin1_General_CP1_CI_AS'))
    DayOfWeek = Column(Integer)
    DateCreated = Column(DateTime)
    LastModifiedBy = Column(Integer)
    DateModified = Column(DateTime)
    CreatedBy = Column(UNIQUEIDENTIFIER)


class ErrorLog(Base):
    __tablename__ = 'ErrorLogs'

    Id = Column(Integer, primary_key=True)
    Message = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    StackTrace = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'))
    Created = Column(DateTime, nullable=False, server_default=text("(getdate())"))
    UserId = Column(UNIQUEIDENTIFIER)


class FileType(Base):
    __tablename__ = 'FileTypes'

    FileTypeId = Column(Integer, primary_key=True)
    Name = Column(String(150, 'SQL_Latin1_General_CP1_CI_AS'))


class Gateway(Base):
    __tablename__ = 'Gateway'

    GatewayID = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), primary_key=True)
    VariantID = Column(Integer, nullable=False)
    GatewayName = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    DateCreated = Column(DateTime, nullable=False)
    BranchID = Column(Integer)
    Signal = Column(Integer)
    Battery = Column(Integer)
    GatewayTypeId = Column(Integer)
    IsActive = Column(Boolean, nullable=False, server_default=text("((1))"))
    LastModifiedBy = Column(Integer)
    DateModified = Column(DateTime)
    CompanyId = Column(Integer)
    CreatedBy = Column(UNIQUEIDENTIFIER)
    ICCID = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    IsDirectGateway = Column(Boolean, nullable=False, server_default=text("((0))"))


class GatewayPort(Base):
    __tablename__ = 'GatewayPorts'

    GatewayPortID = Column(BigInteger, primary_key=True)
    GatewayID = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    PortName = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    DateCreated = Column(DateTime, nullable=False, server_default=text("(getdate())"))
    DateModified = Column(DateTime, server_default=text("(getdate())"))
    LastModifiedBy = Column(Integer)


class GatewayPortsSensor(Base):
    __tablename__ = 'GatewayPortsSensors'

    GatewayPortID = Column(BigInteger, primary_key=True, nullable=False)
    SensorID = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), primary_key=True, nullable=False)


class GatewayShift(Base):
    __tablename__ = 'GatewayShifts'

    GatewayId = Column(Unicode(50), primary_key=True, nullable=False)
    DayOfWeek = Column(Integer, primary_key=True, nullable=False)
    StartTime = Column(Time)
    EndTime = Column(Time)
    IsCustom = Column(Boolean, server_default=text("((0))"))
    DateCreated = Column(DateTime, server_default=text("(getdate())"))
    LastModifiedBy = Column(UNIQUEIDENTIFIER)
    DateModified = Column(DateTime)
    CreatedBy = Column(UNIQUEIDENTIFIER)


class GatewayType(Base):
    __tablename__ = 'GatewayType'

    GatewayTypeID = Column(Integer, primary_key=True)
    TypeName = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))


class GroupSensor(Base):
    __tablename__ = 'GroupSensors'

    GroupId = Column(Integer, primary_key=True, nullable=False)
    SensorId = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), primary_key=True, nullable=False)


class Group(Base):
    __tablename__ = 'Groups'

    GroupId = Column(Integer, primary_key=True)
    GroupName = Column(String(150, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CompanyId = Column(Integer)
    SensorTypeId = Column(Integer)


class Industry(Base):
    __tablename__ = 'Industries'

    Id = Column(Integer, primary_key=True)
    IndustryName = Column(String(150, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)


class Machine(Base):
    __tablename__ = 'Machine'

    MachineID = Column(Integer, primary_key=True)
    MachineName = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    SectorId = Column(Integer)
    Description = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'))
    BranchID = Column(Integer)
    DateModified = Column(DateTime)
    DateCreated = Column(DateTime, nullable=False)
    CompanyId = Column(Integer)
    MachineBlobURl = Column(Unicode)
    LastModifiedBy = Column(UNIQUEIDENTIFIER)
    CreatedBy = Column(UNIQUEIDENTIFIER, nullable=False)
    LocationName = Column(String(225, 'SQL_Latin1_General_CP1_CI_AS'))
    MachineStateId = Column(Integer)
    SN = Column(Unicode(300))


class MachineComment(Base):
    __tablename__ = 'MachineComments'

    Id = Column(Integer, primary_key=True)
    MachineId = Column(Integer)
    CompanyId = Column(Integer)
    UserId = Column(UNIQUEIDENTIFIER)
    Description = Column(Unicode)
    MsgOrder = Column(Integer)
    CreatedBy = Column(UNIQUEIDENTIFIER)
    DateCreated = Column(DateTime)
    DateModified = Column(DateTime)
    LastModifiedBy = Column(UNIQUEIDENTIFIER)
    ReportId = Column(Integer)
    IsFile = Column(Boolean, nullable=False, server_default=text("((0))"))


class MachineFile(Base):
    __tablename__ = 'MachineFiles'

    Id = Column(Integer, primary_key=True)
    MachineId = Column(Integer)
    FileBlobUrl = Column(Unicode)
    DateModified = Column(DateTime)
    DateCreated = Column(DateTime, nullable=False)
    LastModifiedBy = Column(UNIQUEIDENTIFIER)
    CreatedBy = Column(UNIQUEIDENTIFIER, nullable=False)


class MachineIncident(Base):
    __tablename__ = 'MachineIncidents'

    Id = Column(Integer, primary_key=True)
    MachineId = Column(Integer)
    CompanyId = Column(Integer)
    UserId = Column(UNIQUEIDENTIFIER)
    Description = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'))
    CreatedBy = Column(UNIQUEIDENTIFIER)
    DateCreated = Column(DateTime)
    DateModified = Column(DateTime)
    LastModifiedBy = Column(UNIQUEIDENTIFIER)
    MainIncidentId = Column(Integer)


class MachineLocation(Base):
    __tablename__ = 'MachineLocations'

    MachineLocationId = Column(Integer, primary_key=True)
    MachineId = Column(Integer, nullable=False)
    LocationName = Column(String(150, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    DateModified = Column(DateTime)
    LastModifiedBy = Column(Integer)
    DateCreated = Column(DateTime)
    CreatedBy = Column(UNIQUEIDENTIFIER)


class MachineMainIncident(Base):
    __tablename__ = 'MachineMainIncidents'

    Id = Column(Integer, primary_key=True)
    MachineId = Column(Integer)
    CompanyId = Column(Integer)
    ReportTypeId = Column(Integer)
    MachineStateId = Column(Integer)
    CreatedBy = Column(UNIQUEIDENTIFIER)
    DateCreated = Column(DateTime)
    DateModified = Column(DateTime)
    LastModifiedBy = Column(UNIQUEIDENTIFIER)
    IsResolved = Column(Boolean, nullable=False, server_default=text("((0))"))
    ResolvedDate = Column(DateTime)


class MachineOperator(Base):
    __tablename__ = 'MachineOperators'

    MachineId = Column(Integer, primary_key=True, nullable=False)
    UserId = Column(UNIQUEIDENTIFIER, primary_key=True, nullable=False)


class MachineStateHistory(Base):
    __tablename__ = 'MachineStateHistory'

    MachineStateHistoryId = Column(Integer, primary_key=True)
    MachineId = Column(Integer, nullable=False)
    MachineStateId = Column(Integer, nullable=False)
    StartDate = Column(DateTime, nullable=False)
    EndDate = Column(DateTime)
    DateCreated = Column(DateTime, nullable=False)
    CreatedBy = Column(UNIQUEIDENTIFIER, nullable=False)
    ModifyDate = Column(DateTime)
    ModifyBy = Column(UNIQUEIDENTIFIER)
    TriggerBySensorId = Column(Unicode(250))


class MachineState(Base):
    __tablename__ = 'MachineStates'

    StateID = Column(Integer, primary_key=True)
    StateName = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    SortOrder = Column(Integer)
    DateCreated = Column(DateTime, nullable=False)
    DateModified = Column(DateTime)
    CreatedBy = Column(UNIQUEIDENTIFIER)
    IsGenerateReport = Column(Boolean, server_default=text("((0))"))
    CompanyID = Column(Integer)
    Color = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    LastModifiedBy = Column(UNIQUEIDENTIFIER)


class MachineTechnician(Base):
    __tablename__ = 'MachineTechnicians'

    MachineId = Column(Integer, primary_key=True, nullable=False)
    UserId = Column(UNIQUEIDENTIFIER, primary_key=True, nullable=False)
    Description = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    IsResolved = Column(Boolean, server_default=text("((0))"))
    IsAchknowledged = Column(Boolean, server_default=text("((0))"))
    IsNotifyMe = Column(Boolean)
    CreatedBy = Column(UNIQUEIDENTIFIER)
    ReportId = Column(Integer, primary_key=True, nullable=False)
    DateCreated = Column(DateTime)
    DateAcknowleged = Column(DateTime)
    DateResolved = Column(DateTime)
    IsCustomReport = Column(Boolean)


class NotificationTemplate(Base):
    __tablename__ = 'NotificationTemplates'

    NotificationTemplateId = Column(Integer, primary_key=True)
    NotificationTemplateName = Column(String(500, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    UserId = Column(UNIQUEIDENTIFIER)
    IsSMS = Column(Boolean, nullable=False)
    IsCall = Column(Boolean, nullable=False)
    IsEmail = Column(Boolean, nullable=False)
    IsPushNotification = Column(Boolean, nullable=False)
    CreatedBy = Column(UNIQUEIDENTIFIER)
    DateCreated = Column(DateTime)
    DateModified = Column(DateTime)
    LastModifiedBy = Column(UNIQUEIDENTIFIER)
    CompanyId = Column(Integer)
    Description = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'))


class NotificationType(Base):
    __tablename__ = 'NotificationType'

    TypeId = Column(Integer, primary_key=True)
    Name = Column(Unicode(200), nullable=False)


class OtherRole(Base):
    __tablename__ = 'OtherRoles'

    RoleId = Column(UNIQUEIDENTIFIER, primary_key=True)
    RoleType = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)


class PlanFeature(Base):
    __tablename__ = 'PlanFeatures'

    Id = Column(Integer, primary_key=True)
    PricingPlanId = Column(Integer)
    NoOfRecords = Column(Integer, server_default=text("((0))"))
    NoOfSms = Column(Integer, server_default=text("((0))"))
    NoOfCalls = Column(Integer, server_default=text("((0))"))
    IsActive = Column(Boolean, server_default=text("((0))"))
    CreatedBy = Column(UNIQUEIDENTIFIER)
    DateCreated = Column(DateTime)
    DateModified = Column(DateTime)
    LastModifiedBy = Column(UNIQUEIDENTIFIER)


class PricingPlan(Base):
    __tablename__ = 'PricingPlan'

    PlanID = Column(Integer, primary_key=True)
    PlanName = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    AccessId = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    DateCreated = Column(DateTime)
    DateModified = Column(DateTime)
    CreatedBy = Column(UNIQUEIDENTIFIER)
    Price = Column(DECIMAL(10, 2))
    LastModifiedBy = Column(UNIQUEIDENTIFIER)


class ReportCollaborator(Base):
    __tablename__ = 'ReportCollaborators'

    Id = Column(Integer, primary_key=True)
    UserId = Column(UNIQUEIDENTIFIER, nullable=False)
    ReportId = Column(Integer, nullable=False)
    DateCreated = Column(DateTime, nullable=False)
    DateModified = Column(DateTime, nullable=False)


class ReportFile(Base):
    __tablename__ = 'ReportFiles'

    ReportFileId = Column(Integer, primary_key=True)
    FileTypeId = Column(Integer, nullable=False)
    BlobUrl = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'))
    CustomReportId = Column(Integer, nullable=False)
    CreatedBy = Column(UNIQUEIDENTIFIER, nullable=False)
    DateCreated = Column(DateTime)
    DateModified = Column(DateTime)
    LastModifiedBy = Column(UNIQUEIDENTIFIER)


class ReportType(Base):
    __tablename__ = 'ReportType'

    Id = Column(Integer, primary_key=True)
    Name = Column(String(500, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedBy = Column(UNIQUEIDENTIFIER)
    DateCreated = Column(DateTime)
    DateModified = Column(DateTime)
    LastModifiedBy = Column(UNIQUEIDENTIFIER)


class Role(Base):
    __tablename__ = 'Role'

    RoleID = Column(Integer, primary_key=True)
    RoleName = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    DateCreated = Column(DateTime)
    DateModified = Column(DateTime)
    LastModifiedBy = Column(Integer)
    CreatedBy = Column(UNIQUEIDENTIFIER)


class Sector(Base):
    __tablename__ = 'Sectors'

    SectorId = Column(Integer, primary_key=True)
    Name = Column(String(150, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CompanyId = Column(Integer)
    DateCreated = Column(DateTime)
    DateModified = Column(DateTime)
    LastModifiedBy = Column(UNIQUEIDENTIFIER)
    CreatedBy = Column(UNIQUEIDENTIFIER)


class Sensor(Base):
    __tablename__ = 'Sensor'

    SensorID = Column(String(150, 'SQL_Latin1_General_CP1_CI_AS'), primary_key=True)
    SensorName = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    MachineID = Column(Integer)
    SensorTypeID = Column(Integer)
    FrequencyNumber = Column(Integer)
    CriticalMin = Column(DECIMAL(18, 2))
    CriticalMax = Column(DECIMAL(18, 2))
    WarningMin = Column(DECIMAL(18, 2))
    WarningMax = Column(DECIMAL(18, 2))
    DataTypeID = Column(Integer)
    CustomEquation = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    SleepStart = Column(Time)
    SleepEnd = Column(Time)
    DigitalAlarm = Column(Boolean)
    DateCreated = Column(DateTime)
    DigitalLowMin = Column(DECIMAL(18, 0))
    DigitalLowMax = Column(DECIMAL(18, 0))
    DigitalHighMin = Column(DECIMAL(18, 0))
    DigitalHighMax = Column(DECIMAL(18, 0))
    DateModified = Column(DateTime)
    LastModifiedBy = Column(Integer)
    SensorTemplateID = Column(Integer)
    VoltageCriticalMin = Column(DECIMAL(18, 2))
    VoltageCriticalMax = Column(DECIMAL(18, 2))
    VoltageWarningMin = Column(DECIMAL(18, 2))
    VoltageWarningMax = Column(DECIMAL(18, 2))
    CriticalityTypeId = Column(Integer)
    ComingUnitId = Column(Integer)
    Description = Column(String(500, 'SQL_Latin1_General_CP1_CI_AS'))
    SensorTypeUnitId = Column(Integer)
    CompanyId = Column(Integer)
    SensorBlobURl = Column(Unicode)
    CreatedBy = Column(UNIQUEIDENTIFIER)
    MachineLocationId = Column(Integer)
    FrequencyNumberUnit = Column(Integer)
    IsActive = Column(Boolean)
    InactiveDate = Column(DateTime)
    PortNumber = Column(Integer)
    NotificationTemplateId = Column(Integer)
    CriticalMinState = Column(Integer)
    CriticalMaxState = Column(Integer)
    WarningMinState = Column(Integer)
    WarningMaxState = Column(Integer)
    HighActivation = Column(DECIMAL(18, 2))
    BinaryStateId = Column(Integer)
    OnStateId = Column(Integer)
    OffStateId = Column(Integer)
    ReverseEquation = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    SensorHardwareTypeId = Column(Integer)
    IsSensyrtechProvidedSensor = Column(Boolean)
    GatewayID = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    MinFrequency = Column(Integer)
    MaxFrequency = Column(Integer)
    OnMuteNotification = Column(Boolean, nullable=False)
    OffMuteNotification = Column(Boolean, nullable=False)
    Battery = Column(Integer)
    Signal = Column(Integer)
    OnAlarm = Column(Boolean)
    OffAlarm = Column(Boolean)


t_SensorAssociatedTemplate = Table(
    'SensorAssociatedTemplate', metadata,
    Column('NotificationTemplateId', Integer, nullable=False),
    Column('UserId', UNIQUEIDENTIFIER, nullable=False),
    Column('SensorId', String(150, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
)


t_SensorFiles = Table(
    'SensorFiles', metadata,
    Column('SensorFileId', BigInteger, nullable=False),
    Column('SensorId', String(150, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('FileUrl', Unicode, nullable=False),
    Column('DateCreated', DateTime),
    Column('DateModified', DateTime),
    Column('CreatedBy', UNIQUEIDENTIFIER),
    Column('LastModifiedBY', UNIQUEIDENTIFIER)
)


class SensorHardwareType(Base):
    __tablename__ = 'SensorHardwareTypes'

    Id = Column(Integer, primary_key=True)
    Name = Column(String(500, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("('')"))


class SensorHistory(Base):
    __tablename__ = 'SensorHistory'

    SensorHistoryID = Column(Integer, primary_key=True)
    SensorID = Column(String(150, 'SQL_Latin1_General_CP1_CI_AS'))
    Voltage = Column(DECIMAL(9, 2))
    Value = Column(DECIMAL(18, 2))
    SensorStatusID = Column(Integer)
    DateTime = Column(DateTime)
    AVG = Column(DECIMAL(18, 2))
    MIN = Column(DECIMAL(18, 2))
    MAX = Column(DECIMAL(18, 2))
    TimeElapsed = Column(Integer, nullable=False, server_default=text("((0))"))
    OriginalMachineStateId = Column(Integer)
    IsDefaultEntry = Column(Boolean, nullable=False, server_default=text("((0))"))
    ReportId = Column(Integer)
    CurrentMachineStateId = Column(Integer)


class SensorHistoryLog(Base):
    __tablename__ = 'SensorHistoryLogs'

    SensorHistoryLogID = Column(Integer, primary_key=True)
    SensorHistoryID = Column(Integer, nullable=False)
    SensorID = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    Voltage = Column(DECIMAL(9, 2))
    Value = Column(DECIMAL(18, 2))
    SensorStatusID = Column(Integer)
    DateTime = Column(DateTime)
    AVG = Column(DECIMAL(18, 2))
    MIN = Column(DECIMAL(18, 2))
    MAX = Column(DECIMAL(18, 2))
    TimeElapsed = Column(Integer, nullable=False)
    CreatedDate = Column(DateTime, nullable=False, server_default=text("(getdate())"))
    ReportId = Column(Integer)
    OriginalMachineStateId = Column(Integer)


class SensorStatu(Base):
    __tablename__ = 'SensorStatus'

    SensorStatusID = Column(Integer, primary_key=True)
    SensorStatusName = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    DateCreated = Column(DateTime)
    DateModified = Column(DateTime)
    LastModifiedBy = Column(Integer)


class SensorTemplate(Base):
    __tablename__ = 'SensorTemplate'

    SensorTemplateID = Column(Integer, primary_key=True)
    SensorTemplateName = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CustomEquation = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    SensorTypeID = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    DataType = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    DigitalLowMin = Column(DECIMAL(18, 4))
    DigitalLowMax = Column(DECIMAL(18, 4))
    DigitalHighMin = Column(DECIMAL(18, 4))
    DigitalHighMax = Column(DECIMAL(18, 4))
    DateCreated = Column(DateTime)
    DateModified = Column(DateTime)
    LastModifiedBy = Column(Integer)


class SensorThreshold(Base):
    __tablename__ = 'SensorThresholds'

    ThresholdId = Column(Integer, primary_key=True, nullable=False, server_default=text("((0))"))
    SensorId = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'), primary_key=True, nullable=False, server_default=text("('')"))
    Value = Column(DECIMAL(10, 4))
    MachineStateId = Column(Integer)
    CreatedBy = Column(UNIQUEIDENTIFIER)
    DateCreated = Column(DateTime)
    DateModified = Column(DateTime)
    LastModifiedBy = Column(UNIQUEIDENTIFIER)


class SensorType(Base):
    __tablename__ = 'SensorType'

    SensorTypeID = Column(Integer, primary_key=True)
    SensorTypeName = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    DateCreated = Column(DateTime)
    DateModified = Column(DateTime)
    LastModifiedBy = Column(Integer)
    CompanyId = Column(Integer)
    SensorTypeBlobUrl = Column(Unicode)
    CreatedBy = Column(UNIQUEIDENTIFIER)


class SensorTypeUnit(Base):
    __tablename__ = 'SensorTypeUnits'

    SensorTypeUnitId = Column(Integer, primary_key=True)
    UnitName = Column(String(150, 'SQL_Latin1_General_CP1_CI_AS'))
    SensorTypeId = Column(Integer)
    Alias = Column(String(150, 'SQL_Latin1_General_CP1_CI_AS'))
    FuncName = Column(String(150, 'SQL_Latin1_General_CP1_CI_AS'))


class SmsHistory(Base):
    __tablename__ = 'SmsHistory'

    Id = Column(Integer, primary_key=True)
    UserId = Column(UNIQUEIDENTIFIER)
    CompanyId = Column(Integer)
    Description = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'), server_default=text("('')"))
    CreatedBy = Column(UNIQUEIDENTIFIER)
    DateCreated = Column(DateTime)
    DateModified = Column(DateTime)
    LastModifiedBy = Column(UNIQUEIDENTIFIER)


class TechnicianSensorsResolvedHistory(Base):
    __tablename__ = 'TechnicianSensorsResolvedHistory'

    Id = Column(Integer, primary_key=True)
    SensorHistoryId = Column(Integer, nullable=False)
    SensorId = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    ResolvedOn = Column(DateTime, nullable=False, server_default=text("(getdate())"))
    UserId = Column(UNIQUEIDENTIFIER, nullable=False)


class Threshold(Base):
    __tablename__ = 'Thresholds'

    Id = Column(Integer, primary_key=True)
    Name = Column(String(500, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("('')"))
    Color = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("('')"))
    Islow = Column(Boolean, nullable=False, server_default=text("((0))"))
    CompanyId = Column(Integer)
    CreatedBy = Column(UNIQUEIDENTIFIER)
    DateCreated = Column(DateTime)
    DateModified = Column(DateTime)
    LastModifiedBy = Column(UNIQUEIDENTIFIER)


class TimeZone(Base):
    __tablename__ = 'TimeZones'

    TimeZoneId = Column(Integer, primary_key=True)
    GMT = Column(String(150, 'SQL_Latin1_General_CP1_CI_AS'))
    TimeZoneName = Column(String(150, 'SQL_Latin1_General_CP1_CI_AS'))
    StandardName = Column(String(150, 'SQL_Latin1_General_CP1_CI_AS'))


class Transaction(Base):
    __tablename__ = 'Transactions'

    Id = Column(Integer, primary_key=True)
    Receipt = Column(String(500, 'SQL_Latin1_General_CP1_CI_AS'))
    PlanId = Column(Integer, nullable=False)
    Amount = Column(DECIMAL(10, 2), nullable=False)
    CardName = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'))
    ReceiptId = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'))
    Status = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    IsDeleted = Column(Boolean, nullable=False, server_default=text("((0))"))
    CreatedDate = Column(DateTime, nullable=False, server_default=text("(getdate())"))
    CompanyId = Column(Integer)


class User(Base):
    __tablename__ = 'User'

    UserID = Column(Integer, primary_key=True)
    FirstName = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    LastName = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    Email = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    PhoneNumber = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    RoleID = Column(Integer, nullable=False)
    PhoneNotifications = Column(Boolean, nullable=False)
    EmailNotifications = Column(Boolean, nullable=False)
    BranchID = Column(Integer)


class UserAppAcces(Base):
    __tablename__ = 'UserAppAccess'

    Id = Column(Integer, primary_key=True)
    RoleId = Column(UNIQUEIDENTIFIER, nullable=False)
    CanAdd = Column(Boolean, nullable=False)
    CanEdit = Column(Boolean, nullable=False)
    CanDelete = Column(Boolean, nullable=False)
    DateCreated = Column(DateTime)
    DateModified = Column(DateTime)
    LastModifiedBy = Column(UNIQUEIDENTIFIER)
    CreatedBy = Column(UNIQUEIDENTIFIER)


class UserAsset(Base):
    __tablename__ = 'UserAssets'

    UserId = Column(UNIQUEIDENTIFIER, primary_key=True, nullable=False)
    MachineId = Column(Integer, primary_key=True, nullable=False)
    DateCreated = Column(DateTime, server_default=text("(getdate())"))
    LastModifiedBy = Column(UNIQUEIDENTIFIER)
    DateModified = Column(DateTime)
    CreatedBy = Column(UNIQUEIDENTIFIER)


t_UserInvitations = Table(
    'UserInvitations', metadata,
    Column('Id', UNIQUEIDENTIFIER, nullable=False, server_default=text("(newid())")),
    Column('CompanyId', BigInteger),
    Column('UserEmail', Unicode(300), nullable=False),
    Column('RoleId', UNIQUEIDENTIFIER, nullable=False),
    Column('IsReminded', Boolean, nullable=False, server_default=text("((0))")),
    Column('IsPending', Boolean, nullable=False, server_default=text("((1))")),
    Column('DateCreated', DateTime, server_default=text("(getdate())")),
    Column('LastModifiedBy', UNIQUEIDENTIFIER),
    Column('DateModified', DateTime),
    Column('CreatedBy', UNIQUEIDENTIFIER),
    Column('EmailCodeExpiryDateTime', DateTime),
    Column('EmailConfirmationCode', String(150, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ReminderDate', DateTime),
    Column('IsCancel', Boolean)
)


class UserNotificationTemplate(Base):
    __tablename__ = 'UserNotificationTemplates'

    NotificationTemplateId = Column(Integer, primary_key=True, nullable=False)
    UserId = Column(UNIQUEIDENTIFIER, primary_key=True, nullable=False)
    CompanyId = Column(Integer, nullable=False)
    IsSMS = Column(Boolean, nullable=False)
    IsCall = Column(Boolean, nullable=False)
    IsEmail = Column(Boolean, nullable=False)
    IsPushNotification = Column(Boolean, nullable=False)
    CreatedBy = Column(UNIQUEIDENTIFIER)
    DateCreated = Column(DateTime)
    DateModified = Column(DateTime)
    LastModifiedBy = Column(UNIQUEIDENTIFIER)


class UserNotification(Base):
    __tablename__ = 'UserNotifications'

    Id = Column(Integer, primary_key=True)
    Description = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'))
    TaggedUserId = Column(UNIQUEIDENTIFIER)
    CommentsId = Column(Integer)
    CreatedBy = Column(UNIQUEIDENTIFIER)
    DateCreated = Column(DateTime)
    DateModified = Column(DateTime)
    LastModifiedBy = Column(UNIQUEIDENTIFIER)
    IsRead = Column(Boolean, server_default=text("((0))"))


class UserShift(Base):
    __tablename__ = 'UserShifts'

    UserId = Column(UNIQUEIDENTIFIER, primary_key=True, nullable=False)
    DayOfWeek = Column(Integer, primary_key=True, nullable=False)
    StartTime = Column(Time)
    EndTime = Column(Time)
    IsCustom = Column(Boolean, server_default=text("((0))"))
    DateCreated = Column(DateTime, server_default=text("(getdate())"))
    LastModifiedBy = Column(UNIQUEIDENTIFIER)
    DateModified = Column(DateTime)
    CreatedBy = Column(UNIQUEIDENTIFIER)


class VariantType(Base):
    __tablename__ = 'VariantType'

    VariantID = Column(Integer, primary_key=True)
    VariantDescription = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'))
    NumberOfPorts = Column(Integer, nullable=False)
    DateCreated = Column(DateTime)
    DateModified = Column(DateTime)
    LastModifiedBy = Column(Integer)


t_table_name = Table(
    'table_name', metadata,
    Column('RowNum', DECIMAL(10, 4)),
    Column('LocalDate', String(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('LocalTime', String(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TagsData_Log_Text_String', String(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TagsAlarmT_101_Scaled', DECIMAL(10, 4)),
    Column('TagsAlarmT_102_Scaled', DECIMAL(10, 4)),
    Column('TagsAlarmT_103_Scaled', DECIMAL(10, 4)),
    Column('TagsAlarmT_104_Scaled', DECIMAL(10, 4)),
    Column('TagsLT_592_Scaled', DECIMAL(10, 4)),
    Column('TagsLT_593_Scaled', DECIMAL(10, 4)),
    Column('TagsPDT_193_Scaled', DECIMAL(10, 4)),
    Column('TagsTemperatureT_194_Scaled', DECIMAL(10, 4)),
    Column('TagsPressureT_195_Scaled', DECIMAL(10, 4)),
    Column('TagsTemperatureT_198_Scaled', DECIMAL(10, 4)),
    Column('TagsFlowrateT_199_Scaled', DECIMAL(10, 4)),
    Column('TagsPressureT_201_Scaled', DECIMAL(10, 4)),
    Column('TagsFlowrateT_290_Scaled', DECIMAL(10, 4)),
    Column('TagsPressureT_294_Scaled', DECIMAL(10, 4)),
    Column('TagsFlowrateT_298_Scaled', DECIMAL(10, 4)),
    Column('TagsPressureT_296_Scaled', DECIMAL(10, 4)),
    Column('TagsTemperatureT_297_Scaled', DECIMAL(10, 4)),
    Column('TagsPressureT_398_Scaled', DECIMAL(10, 4)),
    Column('TagsFlowrateT_409_Scaled', DECIMAL(10, 4)),
    Column('TagsPressureT_402_Scaled', DECIMAL(10, 4)),
    Column('TagsFlowrateT_405_Scaled', DECIMAL(10, 4)),
    Column('TagsTemperatureT_406_Scaled', DECIMAL(10, 4)),
    Column('TagsAlarmT_105_Scaled', DECIMAL(10, 4)),
    Column('TagsXV110_Status', DECIMAL(10, 4)),
    Column('TagsXV409_Status', DECIMAL(10, 4)),
    Column('TagsXV594_Status', DECIMAL(10, 4)),
    Column('TagsXV595_Status', DECIMAL(10, 4)),
    Column('TagsXV407_Status', DECIMAL(10, 4)),
    Column('TagsXV408_Status', DECIMAL(10, 4)),
    Column('TagsFIC_199CV', DECIMAL(10, 4)),
    Column('TagsFIC_199Auto', DECIMAL(10, 4)),
    Column('TagsFIC_199SP', DECIMAL(10, 4)),
    Column('TagsPIC_120CV', DECIMAL(10, 4)),
    Column('TagsPIC_120Auto', DECIMAL(10, 4)),
    Column('TagsPIC_120SP', DECIMAL(10, 4)),
    Column('TagsPIC_294CV', DECIMAL(10, 4)),
    Column('TagsPIC_294Auto', DECIMAL(10, 4)),
    Column('TagsPIC_294SP', DECIMAL(10, 4)),
    Column('TagsPIC_402CV', DECIMAL(10, 4)),
    Column('TagsPIC_402Auto', DECIMAL(10, 4)),
    Column('TagsPIC_402SP', DECIMAL(10, 4)),
    Column('TagsPIC_398CV', DECIMAL(10, 4)),
    Column('TagsPIC_398Auto', DECIMAL(10, 4)),
    Column('TagsPIC_398SP', DECIMAL(10, 4)),
    Column('TagsTIC_198CV', DECIMAL(10, 4)),
    Column('TagsTIC_198Auto', DECIMAL(10, 4)),
    Column('TagsTIC_198SP', DECIMAL(10, 4)),
    Column('TagsInterlockTrigger', DECIMAL(10, 4))
)


class Order(Base):
    __tablename__ = 'Orders'

    OrderID = Column(Integer, primary_key=True)
    OrderNumber = Column(Integer, nullable=False)
    SensorID = Column(ForeignKey('Sensor.SensorID'))

    Sensor = relationship('Sensor')

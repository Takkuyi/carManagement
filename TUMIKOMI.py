from typing import List, Optional

from sqlalchemy import Column, DECIMAL, Date, DateTime, Enum, ForeignKeyConstraint, Index, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import BIT, INTEGER, MEDIUMTEXT, SMALLINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
import decimal

class Base(DeclarativeBase):
    pass


class Mクレート重量マスタ(Base):
    __tablename__ = 'm_クレート重量マスタ'

    fld_クレート種別: Mapped[str] = mapped_column(String(255))
    id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    fld_重量: Mapped[Optional[int]] = mapped_column(SMALLINT(6))


class Mコースgマスタ(Base):
    __tablename__ = 'm_コースgマスタ'

    fld_グループID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    fld_コースID: Mapped[Optional[int]] = mapped_column(SMALLINT(6))
    fld_コースグループID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    fld_得意先コード: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    fld_得意先名: Mapped[Optional[str]] = mapped_column(String(255))


class Mコースマスタ(Base):
    __tablename__ = 'm_コースマスタ'

    fld_コースID: Mapped[int] = mapped_column(SMALLINT(6), primary_key=True)
    fld_コース名: Mapped[Optional[str]] = mapped_column(String(255))
    fld_車格: Mapped[Optional[str]] = mapped_column(String(255))
    fld_積み方ID: Mapped[Optional[str]] = mapped_column(String(255))
    fld_KR便名: Mapped[Optional[str]] = mapped_column(String(255))
    fld_仕分日係数: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class M取引先マスタ(Base):
    __tablename__ = 'm_取引先マスタ'

    fld_取引先ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    fld_会社名: Mapped[Optional[str]] = mapped_column(String(255))


class M増便報告データ(Base):
    __tablename__ = 'm_増便報告データ'

    増便コース: Mapped[str] = mapped_column(String(255), primary_key=True)
    ID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    増便理由: Mapped[Optional[str]] = mapped_column(String(255))


t_m_社員マスタ = Table(
    'm_社員マスタ', Base.metadata,
    Column('ID', INTEGER(11)),
    Column('fld_氏名', String(255)),
    Column('fld_氏名カナ', String(255)),
    Column('fld_ステータス', String(255)),
    Column('fld_所属', String(255))
)


class M積み方マスタ(Base):
    __tablename__ = 'm_積み方マスタ'

    fld_積み方ID: Mapped[str] = mapped_column(String(255))
    id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    fld_赤PL: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    fld_平PL: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    fld_青PL: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    fld_段PL: Mapped[Optional[int]] = mapped_column(INTEGER(11))


t_m_車両マスタ = Table(
    'm_車両マスタ', Base.metadata,
    Column('fld_車両マスタID', INTEGER(11)),
    Column('fld_車両番号', String(255)),
    Column('fld_状態', String(255)),
    Column('fld_車格', INTEGER(11)),
    Column('fld_初年度登録', DateTime),
    Column('fld_原動機型式', String(255)),
    Column('fld_車名', String(255)),
    Column('fld_車台番号', String(255)),
    Column('fld_車両形式', String(255)),
    Column('fld_自動車種別', String(255)),
    Column('fld_用途', String(255)),
    Column('fld_車両重量', String(255)),
    Column('fld_乗車定員', String(255)),
    Column('fld_最大積載量', SMALLINT(6)),
    Column('fld_車輛重量', SMALLINT(6)),
    Column('fld_車両総重量', SMALLINT(6)),
    Column('fld_長さ', SMALLINT(6)),
    Column('fld_幅', SMALLINT(6)),
    Column('fld_高さ', SMALLINT(6)),
    Column('fld_前前軸重', SMALLINT(6)),
    Column('fld_前後軸重', SMALLINT(6)),
    Column('fld_後前軸重', SMALLINT(6)),
    Column('fld_後後軸重', SMALLINT(6)),
    Column('fld_排気気量', SMALLINT(6)),
    Column('fld_燃料', String(255))
)


t_m_配送先 = Table(
    'm_配送先', Base.metadata,
    Column('fld_配送先ID', INTEGER(11)),
    Column('fld_配送先名', String(255)),
    Column('fld_連絡先', String(255)),
    Column('fld_都道府県', String(255)),
    Column('fld_市区町村', String(255)),
    Column('fld_備考', MEDIUMTEXT),
    Column('fld_荷主', String(255))
)


class M配送先マスタ(Base):
    __tablename__ = 'm_配送先マスタ'

    fld_配送先ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    fld_配送先名: Mapped[Optional[str]] = mapped_column(String(255))
    fld_連絡先: Mapped[Optional[str]] = mapped_column(String(255))
    fld_都道府県: Mapped[Optional[str]] = mapped_column(String(255))
    fld_市区町村: Mapped[Optional[str]] = mapped_column(String(255))


t_t_etc利用料金 = Table(
    't_etc利用料金', Base.metadata,
    Column('ID', INTEGER(11)),
    Column('利用年月日（自）', DateTime),
    Column('時分（自）', DateTime),
    Column('利用年月日（至）', DateTime),
    Column('時分（至）', DateTime),
    Column('利用ＩＣ（自）', String(255)),
    Column('利用ＩＣ（至）', String(255)),
    Column('割引前料金', INTEGER(11)),
    Column('ＥＴＣ割引額', INTEGER(11)),
    Column('通行料金', INTEGER(11)),
    Column('車種', SMALLINT(6)),
    Column('車両番号', SMALLINT(6)),
    Column('ＥＴＣカード番号', String(255)),
    Column('備考', String(255))
)


t_t_整備記録 = Table(
    't_整備記録', Base.metadata,
    Column('整備ID', INTEGER(11)),
    Column('車両マスタID', INTEGER(11)),
    Column('整備日', DateTime),
    Column('整備時走行距離', INTEGER(11)),
    Column('エアクリーナ交換', BIT(1)),
    Column('EOエレメント交換', BIT(1)),
    Column('ミッションデフオイル交換', BIT(1)),
    Column('バッテリー交換', BIT(1))
)


class T積込量データ(Base):
    __tablename__ = 't_積込量データ'

    fld_積込量ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    fld_仕分日: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    fld_コースID: Mapped[Optional[int]] = mapped_column(SMALLINT(6))
    fld_コース内グループ: Mapped[Optional[str]] = mapped_column(String(255))
    fld_赤クレート数: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    fld_平クレート数: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    fld_青クレート数: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    fld_段ボール数: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    fld_学乳数: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    fld_データ入力日: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


t_t_走行距離 = Table(
    't_走行距離', Base.metadata,
    Column('fld_走行距離ID', INTEGER(11)),
    Column('fld_走行車両', INTEGER(11)),
    Column('fld_走行距離', INTEGER(11)),
    Column('fld_給油量', INTEGER(11)),
    Column('fld_登録日', DateTime),
    Column('fld_勤務実績', INTEGER(11))
)


t_t_配送先選択 = Table(
    't_配送先選択', Base.metadata,
    Column('fld_配送日報ID', INTEGER(11)),
    Column('fld_配送先ID', INTEGER(11)),
    Column('fld_選択済み', BIT(1))
)


t_t_配送日報 = Table(
    't_配送日報', Base.metadata,
    Column('fld_配送日報ID', INTEGER(11)),
    Column('fld_社員ID', INTEGER(11)),
    Column('fld_配送日', DateTime),
    Column('fld_車両マスタID', INTEGER(11))
)


class Vehicles(Base):
    __tablename__ = 'vehicles'

    id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    vehicle_number: Mapped[str] = mapped_column(String(20))
    license_plate: Mapped[str] = mapped_column(String(20))
    vehicle_type: Mapped[str] = mapped_column(String(50))
    manufacturer: Mapped[str] = mapped_column(String(50))
    model: Mapped[str] = mapped_column(String(50))
    year_manufactured: Mapped[int] = mapped_column(INTEGER(11))
    date_acquired: Mapped[datetime.date] = mapped_column(Date)
    status: Mapped[str] = mapped_column(Enum('運行中', '整備中', '待機中', '廃車'))
    capacity: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    notes: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text('current_timestamp()'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))

    maintenance_alerts: Mapped[List['MaintenanceAlerts']] = relationship('MaintenanceAlerts', back_populates='vehicle')
    maintenance_records: Mapped[List['MaintenanceRecords']] = relationship('MaintenanceRecords', back_populates='vehicle')
    documents: Mapped[List['Documents']] = relationship('Documents', back_populates='vehicle')


class MaintenanceAlerts(Base):
    __tablename__ = 'maintenance_alerts'
    __table_args__ = (
        ForeignKeyConstraint(['vehicle_id'], ['vehicles.id'], ondelete='CASCADE', name='maintenance_alerts_ibfk_1'),
        Index('vehicle_id', 'vehicle_id')
    )

    id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    vehicle_id: Mapped[int] = mapped_column(INTEGER(11))
    alert_type: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text)
    due_date: Mapped[datetime.date] = mapped_column(Date)
    status: Mapped[str] = mapped_column(Enum('未対応', '対応中', '完了'), server_default=text("'未対応'"))
    priority: Mapped[str] = mapped_column(Enum('低', '中', '高'), server_default=text("'中'"))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text('current_timestamp()'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))

    vehicle: Mapped['Vehicles'] = relationship('Vehicles', back_populates='maintenance_alerts')


class MaintenanceRecords(Base):
    __tablename__ = 'maintenance_records'
    __table_args__ = (
        ForeignKeyConstraint(['vehicle_id'], ['vehicles.id'], ondelete='CASCADE', name='maintenance_records_ibfk_1'),
        Index('vehicle_id', 'vehicle_id')
    )

    id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    vehicle_id: Mapped[int] = mapped_column(INTEGER(11))
    maintenance_type: Mapped[str] = mapped_column(Enum('定期点検', '故障修理', 'オイル交換', 'タイヤ交換', 'その他'))
    description: Mapped[str] = mapped_column(Text)
    maintenance_date: Mapped[datetime.date] = mapped_column(Date)
    status: Mapped[str] = mapped_column(Enum('計画中', '進行中', '完了', 'キャンセル'))
    completion_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    mileage: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    cost: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    performed_by: Mapped[Optional[str]] = mapped_column(String(100))
    vendor: Mapped[Optional[str]] = mapped_column(String(100))
    next_maintenance_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    notes: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text('current_timestamp()'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))

    vehicle: Mapped['Vehicles'] = relationship('Vehicles', back_populates='maintenance_records')
    documents: Mapped[List['Documents']] = relationship('Documents', back_populates='maintenance')
    parts_replacement: Mapped[List['PartsReplacement']] = relationship('PartsReplacement', back_populates='maintenance')


class Documents(Base):
    __tablename__ = 'documents'
    __table_args__ = (
        ForeignKeyConstraint(['maintenance_id'], ['maintenance_records.id'], ondelete='SET NULL', name='documents_ibfk_2'),
        ForeignKeyConstraint(['vehicle_id'], ['vehicles.id'], ondelete='SET NULL', name='documents_ibfk_1'),
        Index('maintenance_id', 'maintenance_id'),
        Index('vehicle_id', 'vehicle_id')
    )

    id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    document_type: Mapped[str] = mapped_column(String(50))
    title: Mapped[str] = mapped_column(String(100))
    file_path: Mapped[str] = mapped_column(String(255))
    vehicle_id: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    maintenance_id: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    uploaded_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text('current_timestamp()'))
    notes: Mapped[Optional[str]] = mapped_column(Text)

    maintenance: Mapped[Optional['MaintenanceRecords']] = relationship('MaintenanceRecords', back_populates='documents')
    vehicle: Mapped[Optional['Vehicles']] = relationship('Vehicles', back_populates='documents')


class PartsReplacement(Base):
    __tablename__ = 'parts_replacement'
    __table_args__ = (
        ForeignKeyConstraint(['maintenance_id'], ['maintenance_records.id'], ondelete='CASCADE', name='parts_replacement_ibfk_1'),
        Index('maintenance_id', 'maintenance_id')
    )

    id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    maintenance_id: Mapped[int] = mapped_column(INTEGER(11))
    part_name: Mapped[str] = mapped_column(String(100))
    quantity: Mapped[int] = mapped_column(INTEGER(11))
    part_number: Mapped[Optional[str]] = mapped_column(String(100))
    cost_per_unit: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    total_cost: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    notes: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text('current_timestamp()'))

    maintenance: Mapped['MaintenanceRecords'] = relationship('MaintenanceRecords', back_populates='parts_replacement')

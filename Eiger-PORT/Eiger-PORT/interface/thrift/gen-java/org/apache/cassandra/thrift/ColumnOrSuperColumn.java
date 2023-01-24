/**
 * Autogenerated by Thrift Compiler (0.7.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 */
package org.apache.cassandra.thrift;

import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.util.EnumMap;
import java.util.Set;
import java.util.HashSet;
import java.util.EnumSet;
import java.util.Collections;
import java.util.BitSet;
import java.nio.ByteBuffer;
import java.util.Arrays;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Methods for fetching rows/records from Cassandra will return either a single instance of ColumnOrSuperColumn or a list
 * of ColumnOrSuperColumns (get_slice()). If you're looking up a SuperColumn (or list of SuperColumns) then the resulting
 * instances of ColumnOrSuperColumn will have the requested SuperColumn in the attribute super_column. For queries resulting
 * in Columns, those values will be in the attribute column. This change was made between 0.3 and 0.4 to standardize on
 * single query methods that may return either a SuperColumn or Column.
 * 
 * If the query was on a counter column family, you will either get a counter_column (instead of a column) or a
 * counter_super_column (instead of a super_column)
 * 
 * @param column. The Column returned by get() or get_slice().
 * @param super_column. The SuperColumn returned by get() or get_slice().
 * @param counter_column. The Counterolumn returned by get() or get_slice().
 * @param counter_super_column. The CounterSuperColumn returned by get() or get_slice().
 */
public class ColumnOrSuperColumn implements org.apache.thrift.TBase<ColumnOrSuperColumn, ColumnOrSuperColumn._Fields>, java.io.Serializable, Cloneable {
  private static final org.apache.thrift.protocol.TStruct STRUCT_DESC = new org.apache.thrift.protocol.TStruct("ColumnOrSuperColumn");

  private static final org.apache.thrift.protocol.TField COLUMN_FIELD_DESC = new org.apache.thrift.protocol.TField("column", org.apache.thrift.protocol.TType.STRUCT, (short)1);
  private static final org.apache.thrift.protocol.TField SUPER_COLUMN_FIELD_DESC = new org.apache.thrift.protocol.TField("super_column", org.apache.thrift.protocol.TType.STRUCT, (short)2);
  private static final org.apache.thrift.protocol.TField COUNTER_COLUMN_FIELD_DESC = new org.apache.thrift.protocol.TField("counter_column", org.apache.thrift.protocol.TType.STRUCT, (short)3);
  private static final org.apache.thrift.protocol.TField COUNTER_SUPER_COLUMN_FIELD_DESC = new org.apache.thrift.protocol.TField("counter_super_column", org.apache.thrift.protocol.TType.STRUCT, (short)4);

  public Column column; // required
  public SuperColumn super_column; // required
  public CounterColumn counter_column; // required
  public CounterSuperColumn counter_super_column; // required

  /** The set of fields this struct contains, along with convenience methods for finding and manipulating them. */
  public enum _Fields implements org.apache.thrift.TFieldIdEnum {
    COLUMN((short)1, "column"),
    SUPER_COLUMN((short)2, "super_column"),
    COUNTER_COLUMN((short)3, "counter_column"),
    COUNTER_SUPER_COLUMN((short)4, "counter_super_column");

    private static final Map<String, _Fields> byName = new HashMap<String, _Fields>();

    static {
      for (_Fields field : EnumSet.allOf(_Fields.class)) {
        byName.put(field.getFieldName(), field);
      }
    }

    /**
     * Find the _Fields constant that matches fieldId, or null if its not found.
     */
    public static _Fields findByThriftId(int fieldId) {
      switch(fieldId) {
        case 1: // COLUMN
          return COLUMN;
        case 2: // SUPER_COLUMN
          return SUPER_COLUMN;
        case 3: // COUNTER_COLUMN
          return COUNTER_COLUMN;
        case 4: // COUNTER_SUPER_COLUMN
          return COUNTER_SUPER_COLUMN;
        default:
          return null;
      }
    }

    /**
     * Find the _Fields constant that matches fieldId, throwing an exception
     * if it is not found.
     */
    public static _Fields findByThriftIdOrThrow(int fieldId) {
      _Fields fields = findByThriftId(fieldId);
      if (fields == null) throw new IllegalArgumentException("Field " + fieldId + " doesn't exist!");
      return fields;
    }

    /**
     * Find the _Fields constant that matches name, or null if its not found.
     */
    public static _Fields findByName(String name) {
      return byName.get(name);
    }

    private final short _thriftId;
    private final String _fieldName;

    _Fields(short thriftId, String fieldName) {
      _thriftId = thriftId;
      _fieldName = fieldName;
    }

    public short getThriftFieldId() {
      return _thriftId;
    }

    public String getFieldName() {
      return _fieldName;
    }
  }

  // isset id assignments

  public static final Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> metaDataMap;
  static {
    Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> tmpMap = new EnumMap<_Fields, org.apache.thrift.meta_data.FieldMetaData>(_Fields.class);
    tmpMap.put(_Fields.COLUMN, new org.apache.thrift.meta_data.FieldMetaData("column", org.apache.thrift.TFieldRequirementType.OPTIONAL, 
        new org.apache.thrift.meta_data.StructMetaData(org.apache.thrift.protocol.TType.STRUCT, Column.class)));
    tmpMap.put(_Fields.SUPER_COLUMN, new org.apache.thrift.meta_data.FieldMetaData("super_column", org.apache.thrift.TFieldRequirementType.OPTIONAL, 
        new org.apache.thrift.meta_data.StructMetaData(org.apache.thrift.protocol.TType.STRUCT, SuperColumn.class)));
    tmpMap.put(_Fields.COUNTER_COLUMN, new org.apache.thrift.meta_data.FieldMetaData("counter_column", org.apache.thrift.TFieldRequirementType.OPTIONAL, 
        new org.apache.thrift.meta_data.StructMetaData(org.apache.thrift.protocol.TType.STRUCT, CounterColumn.class)));
    tmpMap.put(_Fields.COUNTER_SUPER_COLUMN, new org.apache.thrift.meta_data.FieldMetaData("counter_super_column", org.apache.thrift.TFieldRequirementType.OPTIONAL, 
        new org.apache.thrift.meta_data.StructMetaData(org.apache.thrift.protocol.TType.STRUCT, CounterSuperColumn.class)));
    metaDataMap = Collections.unmodifiableMap(tmpMap);
    org.apache.thrift.meta_data.FieldMetaData.addStructMetaDataMap(ColumnOrSuperColumn.class, metaDataMap);
  }

  public ColumnOrSuperColumn() {
  }

  /**
   * Performs a deep copy on <i>other</i>.
   */
  public ColumnOrSuperColumn(ColumnOrSuperColumn other) {
    if (other.isSetColumn()) {
      this.column = new Column(other.column);
    }
    if (other.isSetSuper_column()) {
      this.super_column = new SuperColumn(other.super_column);
    }
    if (other.isSetCounter_column()) {
      this.counter_column = new CounterColumn(other.counter_column);
    }
    if (other.isSetCounter_super_column()) {
      this.counter_super_column = new CounterSuperColumn(other.counter_super_column);
    }
  }

  public ColumnOrSuperColumn deepCopy() {
    return new ColumnOrSuperColumn(this);
  }

  @Override
  public void clear() {
    this.column = null;
    this.super_column = null;
    this.counter_column = null;
    this.counter_super_column = null;
  }

  public Column getColumn() {
    return this.column;
  }

  public ColumnOrSuperColumn setColumn(Column column) {
    this.column = column;
    return this;
  }

  public void unsetColumn() {
    this.column = null;
  }

  /** Returns true if field column is set (has been assigned a value) and false otherwise */
  public boolean isSetColumn() {
    return this.column != null;
  }

  public void setColumnIsSet(boolean value) {
    if (!value) {
      this.column = null;
    }
  }

  public SuperColumn getSuper_column() {
    return this.super_column;
  }

  public ColumnOrSuperColumn setSuper_column(SuperColumn super_column) {
    this.super_column = super_column;
    return this;
  }

  public void unsetSuper_column() {
    this.super_column = null;
  }

  /** Returns true if field super_column is set (has been assigned a value) and false otherwise */
  public boolean isSetSuper_column() {
    return this.super_column != null;
  }

  public void setSuper_columnIsSet(boolean value) {
    if (!value) {
      this.super_column = null;
    }
  }

  public CounterColumn getCounter_column() {
    return this.counter_column;
  }

  public ColumnOrSuperColumn setCounter_column(CounterColumn counter_column) {
    this.counter_column = counter_column;
    return this;
  }

  public void unsetCounter_column() {
    this.counter_column = null;
  }

  /** Returns true if field counter_column is set (has been assigned a value) and false otherwise */
  public boolean isSetCounter_column() {
    return this.counter_column != null;
  }

  public void setCounter_columnIsSet(boolean value) {
    if (!value) {
      this.counter_column = null;
    }
  }

  public CounterSuperColumn getCounter_super_column() {
    return this.counter_super_column;
  }

  public ColumnOrSuperColumn setCounter_super_column(CounterSuperColumn counter_super_column) {
    this.counter_super_column = counter_super_column;
    return this;
  }

  public void unsetCounter_super_column() {
    this.counter_super_column = null;
  }

  /** Returns true if field counter_super_column is set (has been assigned a value) and false otherwise */
  public boolean isSetCounter_super_column() {
    return this.counter_super_column != null;
  }

  public void setCounter_super_columnIsSet(boolean value) {
    if (!value) {
      this.counter_super_column = null;
    }
  }

  public void setFieldValue(_Fields field, Object value) {
    switch (field) {
    case COLUMN:
      if (value == null) {
        unsetColumn();
      } else {
        setColumn((Column)value);
      }
      break;

    case SUPER_COLUMN:
      if (value == null) {
        unsetSuper_column();
      } else {
        setSuper_column((SuperColumn)value);
      }
      break;

    case COUNTER_COLUMN:
      if (value == null) {
        unsetCounter_column();
      } else {
        setCounter_column((CounterColumn)value);
      }
      break;

    case COUNTER_SUPER_COLUMN:
      if (value == null) {
        unsetCounter_super_column();
      } else {
        setCounter_super_column((CounterSuperColumn)value);
      }
      break;

    }
  }

  public Object getFieldValue(_Fields field) {
    switch (field) {
    case COLUMN:
      return getColumn();

    case SUPER_COLUMN:
      return getSuper_column();

    case COUNTER_COLUMN:
      return getCounter_column();

    case COUNTER_SUPER_COLUMN:
      return getCounter_super_column();

    }
    throw new IllegalStateException();
  }

  /** Returns true if field corresponding to fieldID is set (has been assigned a value) and false otherwise */
  public boolean isSet(_Fields field) {
    if (field == null) {
      throw new IllegalArgumentException();
    }

    switch (field) {
    case COLUMN:
      return isSetColumn();
    case SUPER_COLUMN:
      return isSetSuper_column();
    case COUNTER_COLUMN:
      return isSetCounter_column();
    case COUNTER_SUPER_COLUMN:
      return isSetCounter_super_column();
    }
    throw new IllegalStateException();
  }

  @Override
  public boolean equals(Object that) {
    if (that == null)
      return false;
    if (that instanceof ColumnOrSuperColumn)
      return this.equals((ColumnOrSuperColumn)that);
    return false;
  }

  public boolean equals(ColumnOrSuperColumn that) {
    if (that == null)
      return false;

    boolean this_present_column = true && this.isSetColumn();
    boolean that_present_column = true && that.isSetColumn();
    if (this_present_column || that_present_column) {
      if (!(this_present_column && that_present_column))
        return false;
      if (!this.column.equals(that.column))
        return false;
    }

    boolean this_present_super_column = true && this.isSetSuper_column();
    boolean that_present_super_column = true && that.isSetSuper_column();
    if (this_present_super_column || that_present_super_column) {
      if (!(this_present_super_column && that_present_super_column))
        return false;
      if (!this.super_column.equals(that.super_column))
        return false;
    }

    boolean this_present_counter_column = true && this.isSetCounter_column();
    boolean that_present_counter_column = true && that.isSetCounter_column();
    if (this_present_counter_column || that_present_counter_column) {
      if (!(this_present_counter_column && that_present_counter_column))
        return false;
      if (!this.counter_column.equals(that.counter_column))
        return false;
    }

    boolean this_present_counter_super_column = true && this.isSetCounter_super_column();
    boolean that_present_counter_super_column = true && that.isSetCounter_super_column();
    if (this_present_counter_super_column || that_present_counter_super_column) {
      if (!(this_present_counter_super_column && that_present_counter_super_column))
        return false;
      if (!this.counter_super_column.equals(that.counter_super_column))
        return false;
    }

    return true;
  }

  @Override
  public int hashCode() {
    return 0;
  }

  public int compareTo(ColumnOrSuperColumn other) {
    if (!getClass().equals(other.getClass())) {
      return getClass().getName().compareTo(other.getClass().getName());
    }

    int lastComparison = 0;
    ColumnOrSuperColumn typedOther = (ColumnOrSuperColumn)other;

    lastComparison = Boolean.valueOf(isSetColumn()).compareTo(typedOther.isSetColumn());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetColumn()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.column, typedOther.column);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = Boolean.valueOf(isSetSuper_column()).compareTo(typedOther.isSetSuper_column());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetSuper_column()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.super_column, typedOther.super_column);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = Boolean.valueOf(isSetCounter_column()).compareTo(typedOther.isSetCounter_column());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetCounter_column()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.counter_column, typedOther.counter_column);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = Boolean.valueOf(isSetCounter_super_column()).compareTo(typedOther.isSetCounter_super_column());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetCounter_super_column()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.counter_super_column, typedOther.counter_super_column);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    return 0;
  }

  public _Fields fieldForId(int fieldId) {
    return _Fields.findByThriftId(fieldId);
  }

  public void read(org.apache.thrift.protocol.TProtocol iprot) throws org.apache.thrift.TException {
    org.apache.thrift.protocol.TField field;
    iprot.readStructBegin();
    while (true)
    {
      field = iprot.readFieldBegin();
      if (field.type == org.apache.thrift.protocol.TType.STOP) { 
        break;
      }
      switch (field.id) {
        case 1: // COLUMN
          if (field.type == org.apache.thrift.protocol.TType.STRUCT) {
            this.column = new Column();
            this.column.read(iprot);
          } else { 
            org.apache.thrift.protocol.TProtocolUtil.skip(iprot, field.type);
          }
          break;
        case 2: // SUPER_COLUMN
          if (field.type == org.apache.thrift.protocol.TType.STRUCT) {
            this.super_column = new SuperColumn();
            this.super_column.read(iprot);
          } else { 
            org.apache.thrift.protocol.TProtocolUtil.skip(iprot, field.type);
          }
          break;
        case 3: // COUNTER_COLUMN
          if (field.type == org.apache.thrift.protocol.TType.STRUCT) {
            this.counter_column = new CounterColumn();
            this.counter_column.read(iprot);
          } else { 
            org.apache.thrift.protocol.TProtocolUtil.skip(iprot, field.type);
          }
          break;
        case 4: // COUNTER_SUPER_COLUMN
          if (field.type == org.apache.thrift.protocol.TType.STRUCT) {
            this.counter_super_column = new CounterSuperColumn();
            this.counter_super_column.read(iprot);
          } else { 
            org.apache.thrift.protocol.TProtocolUtil.skip(iprot, field.type);
          }
          break;
        default:
          org.apache.thrift.protocol.TProtocolUtil.skip(iprot, field.type);
      }
      iprot.readFieldEnd();
    }
    iprot.readStructEnd();

    // check for required fields of primitive type, which can't be checked in the validate method
    validate();
  }

  public void write(org.apache.thrift.protocol.TProtocol oprot) throws org.apache.thrift.TException {
    validate();

    oprot.writeStructBegin(STRUCT_DESC);
    if (this.column != null) {
      if (isSetColumn()) {
        oprot.writeFieldBegin(COLUMN_FIELD_DESC);
        this.column.write(oprot);
        oprot.writeFieldEnd();
      }
    }
    if (this.super_column != null) {
      if (isSetSuper_column()) {
        oprot.writeFieldBegin(SUPER_COLUMN_FIELD_DESC);
        this.super_column.write(oprot);
        oprot.writeFieldEnd();
      }
    }
    if (this.counter_column != null) {
      if (isSetCounter_column()) {
        oprot.writeFieldBegin(COUNTER_COLUMN_FIELD_DESC);
        this.counter_column.write(oprot);
        oprot.writeFieldEnd();
      }
    }
    if (this.counter_super_column != null) {
      if (isSetCounter_super_column()) {
        oprot.writeFieldBegin(COUNTER_SUPER_COLUMN_FIELD_DESC);
        this.counter_super_column.write(oprot);
        oprot.writeFieldEnd();
      }
    }
    oprot.writeFieldStop();
    oprot.writeStructEnd();
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder("ColumnOrSuperColumn(");
    boolean first = true;

    if (isSetColumn()) {
      sb.append("column:");
      if (this.column == null) {
        sb.append("null");
      } else {
        sb.append(this.column);
      }
      first = false;
    }
    if (isSetSuper_column()) {
      if (!first) sb.append(", ");
      sb.append("super_column:");
      if (this.super_column == null) {
        sb.append("null");
      } else {
        sb.append(this.super_column);
      }
      first = false;
    }
    if (isSetCounter_column()) {
      if (!first) sb.append(", ");
      sb.append("counter_column:");
      if (this.counter_column == null) {
        sb.append("null");
      } else {
        sb.append(this.counter_column);
      }
      first = false;
    }
    if (isSetCounter_super_column()) {
      if (!first) sb.append(", ");
      sb.append("counter_super_column:");
      if (this.counter_super_column == null) {
        sb.append("null");
      } else {
        sb.append(this.counter_super_column);
      }
      first = false;
    }
    sb.append(")");
    return sb.toString();
  }

  public void validate() throws org.apache.thrift.TException {
    // check for required fields
  }

  private void writeObject(java.io.ObjectOutputStream out) throws java.io.IOException {
    try {
      write(new org.apache.thrift.protocol.TCompactProtocol(new org.apache.thrift.transport.TIOStreamTransport(out)));
    } catch (org.apache.thrift.TException te) {
      throw new java.io.IOException(te);
    }
  }

  private void readObject(java.io.ObjectInputStream in) throws java.io.IOException, ClassNotFoundException {
    try {
      read(new org.apache.thrift.protocol.TCompactProtocol(new org.apache.thrift.transport.TIOStreamTransport(in)));
    } catch (org.apache.thrift.TException te) {
      throw new java.io.IOException(te);
    }
  }

}


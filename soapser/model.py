from spyne import Boolean, ComplexModel, Integer, String

from soapser import NAMESPACE

MY_STRING = String(nillable=False)
ComplexModelOrdered = ComplexModel.customize(declare_order='declared',
                                             nillable=False)


class Extensions(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    FieldCode = MY_STRING(min_occurs=1)
    FieldCodeDesc = MY_STRING
    FieldValue = MY_STRING(min_occurs=1)


class ItemBarCode(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    IsPrimary = MY_STRING
    ItemCode = MY_STRING
    Barcode = MY_STRING
    Quantity = MY_STRING(min_occurs=1)
    ActionType = MY_STRING
    BarcodeType = MY_STRING
    Extensions = Extensions.customize(max_occurs='unbounded')


class ItemBarCodeList(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    ItemBarCode = ItemBarCode.customize(max_occurs='unbounded')


class Message(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    ItemBarCodeList = ItemBarCodeList.customize(min_occurs=1)


class Header(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    Message_Type = MY_STRING
    Company_ID = MY_STRING
    Version = MY_STRING
    Source = MY_STRING
    Destination = MY_STRING
    Action_Type = MY_STRING(values=['read', 'write'])
    Sequence_Number = Integer(nillable=False)
    Batch_ID = MY_STRING
    Reference_ID = MY_STRING
    Msg_Locale = MY_STRING
    Msg_Time_Zone = MY_STRING
    Internal_Date_Time_Stamp = MY_STRING(min_occurs=1)


class TXml(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    Header = Header.customize(min_occurs=1)
    Message = Message.customize(min_occurs=1)


class ReceiveItemBarCode(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    tXml = TXml.customize(min_occurs=1)


class ResponseHeader(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    ReturnType = MY_STRING(min_occurs=1)
    ReturnCode = MY_STRING(min_occurs=1)
    ReturnMessage = MY_STRING(min_occurs=1)


class ReceiveItemBarCodeOutput(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    receiveItemBarCodeResult = Boolean(min_occurs=1, nillable=False)
    responseHeader = ResponseHeader

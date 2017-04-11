from spyne import srpc, ServiceBase

from soapser import xml_writer
import soapser.model as mod


class receiveItemBarCodeService(ServiceBase):
    @srpc(mod.ReceiveItemBarCode, _returns=mod.ReceiveItemBarCodeOutput,
          _body_style='bare',
          _operation_name='Flow_Services_Custom_receiveItemBarCode')
    def receiveItemBarCode(receiveItemBarCode):
        xml_writer.write_xml(receiveItemBarCode)
        return mod.ReceiveItemBarCodeOutput(
            receiveItemBarCodeResult=True,
            responseHeader=mod.ResponseHeader(
                ReturnType='rt1', ReturnCode='rc1', ReturnMessage='rm1')
            )

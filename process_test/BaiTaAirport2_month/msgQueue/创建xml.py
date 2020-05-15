# coding:utf-8
import xml.etree.ElementTree as ET



def add_xml(root, tag, text,attrib={}):
    ele = ET.SubElement(root, tag,attrib)
    ele.attrib = attrib
    ele.text = text
    # ele.attrib = attrib
    ele.tail = "\n"

root = ET.Element("Message",
                  {"xmlns:i": "http://www.w3.org/2001/XMLSchema-instance",
                   "xmlns": "http://schemas.datacontract.org/2004/07/Xasd.FASC.SECM.Entity"})

SysID = root.makeelement("SysID", {})
searchID = root.makeelement("searchID", {})
InfoType = root.makeelement("InfoType", {})
Records = root.makeelement("Records", {})
Record = Records.makeelement("Record", {})
Status = Record.makeelement("Status", {})
lk_IsInternation = Record.makeelement("lk_IsInternation", {})
lk_bdno = Record.makeelement("lk_bdno", {})
lk_card = Record.makeelement("lk_card", {})
lk_cardid = Record.makeelement("lk_cardid", {})
lk_chkn = Record.makeelement("lk_chkn", {})
lk_chkt = Record.makeelement("lk_chkt", {})
lk_class = Record.makeelement("lk_class", {})
lk_cname = Record.makeelement("lk_cname", {})
lk_date = Record.makeelement("lk_date", {})
lk_del = Record.makeelement("lk_del", {})
lk_dest = Record.makeelement("lk_dest", {})
lk_ename = Record.makeelement("lk_ename", {})
lk_flight = Record.makeelement("lk_flight", {})
lk_gateno = Record.makeelement("lk_gateno", {})
lk_id = Record.makeelement("lk_id", {})
lk_inf = Record.makeelement("lk_inf", {})
lk_infname = Record.makeelement("lk_infname", {})
lk_insur = Record.makeelement("lk_insur", {})
lk_nation = Record.makeelement("lk_nation", {})
lk_outtime = Record.makeelement("lk_outtime", {})
lk_resr = Record.makeelement("lk_resr", {})
lk_seat = Record.makeelement("lk_seat", {})
lk_sex = Record.makeelement("lk_sex", {})
lk_strt = Record.makeelement("lk_strt", {})
lk_tel = Record.makeelement("lk_tel", {})
lk_vip = Record.makeelement("lk_vip", {})

add_xml(root, "SysID", "HET01", {})
add_xml(root, "searchID", text="1", attrib={})
add_xml(root, "InfoType", text="lkxxb", attrib={})

add_xml(Records, "records", text="", attrib={})
add_xml(Record, "Status", text="lkxxb", attrib={})
add_xml(Record, "lk_IsInternation", text="2", attrib={})

tree = ET.ElementTree(root)
tree.write("note.xml", encoding="utf-8", xml_declaration=True)
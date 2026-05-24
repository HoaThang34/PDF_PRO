const tools = [
  { name: 'Merge PDF', icon: '📄', desc: 'Gộp nhiều file PDF thành một' },
  { name: 'Split PDF', icon: '✂️', desc: 'Chia nhỏ file PDF theo trang' },
  { name: 'Compress PDF', icon: '📦', desc: 'Giảm kích thước file PDF' },
  { name: 'Convert PDF', icon: '🔄', desc: 'Chuyển đổi sang định dạng khác' },
  { name: 'Edit PDF', icon: '✏️', desc: 'Chỉnh sửa nội dung PDF trực tiếp' },
  { name: 'OCR PDF', icon: '🔍', desc: 'Nhận dạng văn bản từ hình ảnh' },
  { name: 'Watermark', icon: '💧', desc: 'Thêm watermark vào PDF' },
  { name: 'Sign PDF', icon: '✍️', desc: 'Ký số vào file PDF' },
  { name: 'Protect PDF', icon: '🔒', desc: 'Bảo vệ PDF bằng mật khẩu' },
  { name: 'Unlock PDF', icon: '🔓', desc: 'Mở khóa file PDF' },
]

export default function ToolsGrid() {
  return (
    <section className="tools-grid" id="tools">
      <div className="container">
        <div className="section-header">
          <h2>Tất cả công cụ PDF</h2>
          <p>Bộ công cụ toàn diện đáp ứng mọi nhu cầu xử lý PDF của bạn</p>
        </div>
        <div className="tools-grid-inner">
          {tools.map((t) => (
            <div key={t.name} className="tool-card">
              <span className="tool-icon">{t.icon}</span>
              <h3 className="tool-name">{t.name}</h3>
              <p className="tool-desc">{t.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}

const advanced = [
  { title: 'OCR AI', desc: 'Nhận dạng văn bản thông minh từ hình ảnh scan', icon: '🧠' },
  { title: 'Đa ngôn ngữ', desc: 'Hỗ trợ hơn 30 ngôn ngữ khác nhau', icon: '🌐' },
  { title: 'API Integration', desc: 'Tích hợp API để xử lý PDF tự động', icon: '🔌' },
  { title: 'Team workspace', desc: 'Làm việc nhóm với không gian làm việc chung', icon: '👥' },
  { title: 'Sao lưu tự động', desc: 'Tự động sao lưu file vào đám mây', icon: '💾' },
  { title: 'Smart compression', desc: 'Giảm kích thước file thông minh không mất chất lượng', icon: '🎯' },
]

export default function AdvancedFeatures() {
  return (
    <section className="advanced-features">
      <div className="container">
        <div className="section-header">
          <h2>Tính năng nâng cao</h2>
          <p>Những tính năng dành cho người dùng chuyên nghiệp</p>
        </div>
        <div className="advanced-grid">
          {advanced.map((a) => (
            <div key={a.title} className="advanced-card">
              <span className="advanced-icon">{a.icon}</span>
              <h3>{a.title}</h3>
              <p>{a.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}

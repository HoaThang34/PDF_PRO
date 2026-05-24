const stats = [
  { value: '0.5s', label: 'Tốc độ xử lý', desc: 'Trung bình 0.5 giây/file' },
  { value: '2GB', label: 'Dung lượng tối đa', desc: 'Hỗ trợ file lên tới 2GB' },
  { value: '99.9%', label: 'Uptime', desc: 'Hệ thống hoạt động liên tục' },
  { value: '1.2M', label: 'File/ngày', desc: 'Lượng file xử lý mỗi ngày' },
]

export default function PerformanceStats() {
  return (
    <section className="performance-stats">
      <div className="container">
        <div className="section-header">
          <h2>Hiệu suất vượt trội</h2>
          <p>Con số biết nói về sức mạnh của PDF PRO</p>
        </div>
        <div className="stats-grid">
          {stats.map((s) => (
            <div key={s.label} className="stat-card">
              <div className="stat-value gradient-text">{s.value}</div>
              <div className="stat-label">{s.label}</div>
              <div className="stat-desc">{s.desc}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}

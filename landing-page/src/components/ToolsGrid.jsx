import { IconMerge, IconSplit, IconCompress, IconConvert, IconEdit, IconOcr, IconWatermark, IconSign, IconProtect, IconUnlock } from '../icons.jsx'

const tools = [
  {
    name: 'Ghép File PDF (Merge PDF)',
    icon: IconMerge,
    desc: 'Hợp nhất nhiều file PDF riêng lẻ thành một tài liệu duy nhất một cách nhanh chóng. Bạn có thể chọn thứ tự các trang, sắp xếp lại theo ý muốn trước khi tiến hành ghép. Hỗ trợ ghép không giới hạn số lượng file cùng lúc, giúp bạn dễ dàng tổng hợp báo cáo, tài liệu hay hợp đồng từ nhiều nguồn khác nhau mà không lo mất định dạng gốc. Kết quả đầu ra được tối ưu dung lượng nhưng vẫn giữ nguyên chất lượng văn bản và hình ảnh như bản gốc.',
  },
  {
    name: 'Tách Trang PDF (Split PDF)',
    icon: IconSplit,
    desc: 'Chia nhỏ file PDF thành nhiều phần riêng biệt theo từng trang hoặc theo khoảng trang tùy chỉnh. Bạn có thể trích xuất những trang cần thiết từ một tài liệu lớn mà không phải xử lý toàn bộ file. Tính năng hỗ trợ xem trước thumbnail để dễ dàng chọn lựa trang muốn tách. Đặc biệt hữu ích khi bạn chỉ cần một vài trang từ một tài liệu dài hàng trăm trang.',
  },
  {
    name: 'Nén File PDF (Compress PDF)',
    icon: IconCompress,
    desc: 'Giảm kích thước file PDF một cách thông minh với công nghệ nén thế hệ mới. Hệ thống tự động tối ưu hóa hình ảnh, loại bỏ dữ liệu trùng lặp và nén font chữ mà không làm giảm chất lượng hiển thị. Bạn có thể lựa chọn giữa các mức độ nén khác nhau tùy theo nhu cầu: nén nhanh cho file dung lượng nhỏ hoặc nén sâu cho file cần giảm tối đa kích thước.',
  },
  {
    name: 'Chuyển Đổi PDF (Convert PDF)',
    icon: IconConvert,
    desc: 'Chuyển đổi qua lại giữa PDF và các định dạng phổ biến khác như Word, Excel, hình ảnh (PNG/JPEG), văn bản thuần (TXT). Quá trình chuyển đổi diễn ra trong vài giây với độ chính xác cao, giữ nguyên bố cục, font chữ và định dạng gốc. Đặc biệt hỗ trợ chuyển đổi hàng loạt nhiều file cùng lúc, tiết kiệm thời gian tối đa cho công việc của bạn.',
  },
  {
    name: 'Chỉnh Sửa PDF (Edit PDF)',
    icon: IconEdit,
    desc: 'Chỉnh sửa nội dung PDF trực tiếp mà không cần chuyển đổi sang định dạng khác. Bạn có thể thêm, xóa hoặc sửa văn bản, chèn hình ảnh, vẽ hình khối, tô màu, gạch chân và đánh dấu nội dung quan trọng. Tính năng hoàn tác (undo/redo) giúp bạn thoải mái thử nghiệm mà không sợ mất dữ liệu gốc. Giao diện trực quan với thanh công cụ đầy đủ tiện ích.',
  },
  {
    name: 'OCR PDF (Nhận Dạng Văn Bản)',
    icon: IconOcr,
    desc: 'Nhận dạng ký tự quang học (OCR) thông minh sử dụng công nghệ AI, giúp chuyển đổi file PDF được scan từ giấy tờ, sách báo thành văn bản có thể chỉnh sửa được. Hỗ trợ nhận dạng đa ngôn ngữ bao gồm tiếng Việt, tiếng Anh, tiếng Trung và nhiều ngôn ngữ khác. Độ chính xác lên đến 99% với văn bản in rõ ràng, giúp bạn số hóa tài liệu một cách dễ dàng.',
  },
  {
    name: 'Thêm Watermark (Watermark PDF)',
    icon: IconWatermark,
    desc: 'Thêm hình mờ (watermark) chuyên nghiệp vào file PDF để bảo vệ bản quyền tài liệu. Bạn có thể tùy chỉnh nội dung watermark dưới dạng văn bản hoặc hình ảnh, điều chỉnh độ mờ, góc xoay, kích thước và vị trí hiển thị trên từng trang. Hỗ trợ thêm watermark hàng loạt cho nhiều file cùng lúc, phù hợp cho doanh nghiệp cần bảo vệ tài liệu nội bộ.',
  },
  {
    name: 'Ký Số PDF (Sign PDF)',
    icon: IconSign,
    desc: 'Ký tên trực tiếp lên file PDF bằng chuột, bút cảm ứng hoặc tải lên chữ ký mẫu có sẵn. Bạn có thể tạo chữ ký tay tự nhiên, chọn nhiều kiểu chữ ký khác nhau và điều chỉnh kích thước, vị trí phù hợp trên tài liệu. Hỗ trợ thêm nhiều chữ ký trên cùng một file, kèm theo ngày tháng và ghi chú, đáp ứng nhu cầu ký kết hợp đồng, văn bản hành chính.',
  },
  {
    name: 'Bảo Vệ PDF (Protect PDF)',
    icon: IconProtect,
    desc: 'Bảo vệ file PDF bằng mật khẩu với cơ chế mã hóa AES 256-bit tiêu chuẩn quốc tế. Bạn có thể thiết lập hai loại mật khẩu: mật khẩu mở file (User Password) và mật khẩu chỉnh sửa (Owner Password). Hỗ trợ thêm các hạn chế như cấm in ấn, cấm sao chép nội dung, cấm chỉnh sửa để đảm bảo an toàn tuyệt đối cho tài liệu quan trọng.',
  },
  {
    name: 'Mở Khóa PDF (Unlock PDF)',
    icon: IconUnlock,
    desc: 'Mở khóa file PDF đã bị khóa mật khẩu một cách nhanh chóng và an toàn. Hỗ trợ gỡ bỏ mọi loại hạn chế bao gồm mật khẩu mở file, hạn chế in ấn, sao chép và chỉnh sửa. Quá trình giải mã diễn ra hoàn toàn trên máy của bạn, đảm bảo file không bị gửi lên server bên thứ ba, giữ nguyên chất lượng và nội dung gốc của tài liệu.',
  },
]

export default function ToolsGrid() {
  return (
    <section className="tools-grid" id="tools">
      <div className="container">
        <div className="section-header">
          <h2>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" width="28" height="28" style={{ verticalAlign: 'middle', marginRight: 12 }}>
              <rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18" />
              <line x1="7" y1="2" x2="7" y2="6" />
              <line x1="17" y1="2" x2="17" y2="6" />
              <line x1="2" y1="7" x2="22" y2="7" />
            </svg>
            Tất cả công cụ PDF
          </h2>
          <p>Bộ sưu tập 10 công cụ xử lý PDF mạnh mẽ, đáp ứng mọi nhu cầu từ cơ bản đến nâng cao của bạn</p>
        </div>
        <div className="tools-grid-inner">
          {tools.map((t) => (
            <div key={t.name} className="tool-card">
              <span className="tool-icon"><t.icon /></span>
              <h3 className="tool-name">{t.name}</h3>
              <p className="tool-desc">{t.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
